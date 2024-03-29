#coding=utf-8
from django.db import models
from common.models import Person
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_auth_ldap.config import _LDAPConfig
from django_auth_ldap.backend import LDAPSettings
from utils.passwords import get_pronounceable_password, makeSecret
from django.core.mail import send_mail
from django.conf import settings

class Rank(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=12)
    type = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Rango"
    
    def __unicode__(self):
        return self.name

class Firefighter(Person):
    class Meta:
        verbose_name = "Bombero"
        ordering = ['-number', 'last_name']
        
    BLOOD_TYPE_CHOICES = (
        (u'O', u'O'),
        (u'A', u'A'),
        (u'B', u'B'),
        (u'AB', u'AB'),
    )
    
    BLOOD_RH_CHOICES = (
        (u'+', u'Positivo'),
        (u'-', u'Negativo'),
    )
    
    user = models.OneToOneField(User, null=True, blank= True)
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES, null=True, blank=True, verbose_name = u'Factor Sanguineo')
    blood_type_rh = models.CharField(max_length=1, choices=BLOOD_RH_CHOICES, null=True, blank=True, verbose_name = u'RH')
    initials = models.CharField(max_length=4, null=True, blank=True, verbose_name = u'Iniciales')
    number = models.SmallIntegerField(null=True, blank=True, verbose_name = u'Número de Carnet')
    ranks = models.ManyToManyField(Rank, through="RankChange", null=True, verbose_name = u'Rangos')
    
class RankChange(models.Model):
    class Meta:
        verbose_name = "Ascenso"
    
    firefighter = models.ForeignKey(Firefighter)
    rank_obtained = models.ForeignKey(Rank, verbose_name = u'Rango Obtenido')
    date = models.DateField(verbose_name = u'Fecha')
    
    def __unicode__(self):
        return str(self.rank_obtained) + " "+str(self.date)

class Condition(models.Model):
    class Meta:
        verbose_name = u"Condición"
        verbose_name_plural = u"Condiciones"
    
    name = models.CharField(max_length=30, verbose_name = u'Nombre')
    description = models.TextField(null=True, blank = True, verbose_name = u'Descripción')
    
    def __unicode__(self):
        return self.name

class ConditionChange(models.Model):
    class Meta:
        verbose_name = u"Cámbio de Condición"
    
    firefighter = models.ForeignKey(Firefighter, verbose_name = u'Bombero')
    condition = models.ForeignKey(Condition, verbose_name = u'Condición')
    date = models.DateField(verbose_name = u'Fecha')

    def __unicode__(self):
        return str(self.condition) + " "+str(self.date)

class Condecoration(models.Model):
    class Meta:
        verbose_name = u"Condecoración"
        verbose_name_plural = u"Condecoraciones"
    
    name = models.CharField(max_length=30, verbose_name = u'Nombre')
    description = models.TextField(null=True, blank = True, verbose_name = u'Descripción')
    
    def __unicode__(self):
        return self.name

class CondecorationAward(models.Model):
    class Meta:
        verbose_name = u"Otorgamiento de Condecoración"
    
    firefighter = models.ForeignKey(Firefighter, verbose_name = u'Bombero')
    condecoration = models.ForeignKey(Condecoration, verbose_name = u'Condecoración')
    date = models.DateField(verbose_name = u'Fecha')

    def __unicode__(self):
        return str(self.condecoration) + " "+str(self.date)

@receiver(post_save, sender=User)
def join_user_profile(sender, instance, created, **kwargs):
    if created:
        try:
            ff = Firefighter.objects.get(primary_email=instance.username+"@bomberos.usb.ve")
            ff.user = instance
            ff.save()
        except:
            pass
        
if settings.AUTH_LDAP_BIND_PASSWORD:
    @receiver(post_save, sender=Firefighter)
    def create_ldap_user(sender, instance, created, **kwargs):
        if not created:
            return
        
        ldap_c = _LDAPConfig.get_ldap()

        settings = LDAPSettings()
        conn = ldap_c.initialize(settings.AUTH_LDAP_SERVER_URI)
        conn.simple_bind_s(settings.AUTH_LDAP_BIND_DN, settings.AUTH_LDAP_BIND_PASSWORD)
        for opt, value in settings.AUTH_LDAP_CONNECTION_OPTIONS.iteritems():
            conn.set_option(opt, value)
        
        username = instance.first_name[0] + "".join(instance.last_name.split(" "))
        username = str(username.lower())
        uid = gid = 1500+instance.id
        new_password = get_pronounceable_password()
        new_user_group = [
                    ('objectclass', ['posixGroup','top']),
                    ('gidNumber', str(gid)),
                    ]
        try:
            conn.add_s('cn='+str(username)+',ou=groups,dc=bomberos,dc=usb,dc=ve', new_user_group)
        except:
            pass
        
        new_user = [
                    ('objectclass', ['inetOrgPerson','posixAccount', 'top']),
                    ('gidNumber', str(gid)),
                    ('uidNumber', str(uid)),
                    ('sn',  str(instance)),
                    ('givenName',str(instance.first_name.encode('UTF-8'))),
                    ('displayName',  str(instance.first_name.encode('UTF-8'))+" "+str(instance.last_name.encode('UTF-8'))),
                    ('cn',  str(instance.first_name.encode('UTF-8'))+" "+str(instance.last_name.encode('UTF-8'))),
                    ('homeDirectory', str('/home/')+str(username)+'/'),
                    ('loginShell', str('/bin/bash') ),
                    ('userPassword', makeSecret(new_password)),
                    ('mail', str(username)+str("@bomberos.usb.ve")),
                    ]
        
        try:
            conn.add_s('uid='+str(username)+',ou=users,dc=bomberos,dc=usb,dc=ve',new_user)
        except:
            pass
        mod_attrs = [( ldap_c.MOD_ADD, 'memberUid', str(username) )]
        try:
            conn.modify_s('cn=cbvusb,ou=groups,dc=bomberos,dc=usb,dc=ve', mod_attrs)
        except:
            pass
        
        send_welcome_email(str(instance), username, new_password, instance.alternate_email)
        send_webmaster_email(username)
        instance.primary_email = username+"@bomberos.usb.ve"
        instance.save()

def send_welcome_email(name, username, password, email):
    subject = "Bienvenido a CBVUSB-NET"
    content = "Hola "+ name +", has sido agregado al los sistemas de informacion del CBVUSB.\n\nTu informacion de acceso es:\n\nLogin\
: "+username+"\nClave: "+password +    "\n\nVisita http://bomberos.usb.ve/confluence/display/publico/Nuevo+en+la+CBVUSB-NET para mas \
informacion\n\nCualquier duda comunicarse con el administrador via webmaster@bomberos.usb.ve\n\nNOTA: este correo es enviado automati\
camente por el servidor.\n\n--\nwebmaster\nCBVUSB"
    send_mail(subject, content, settings.DEFAULT_FROM_EMAIL, [email,], fail_silently=True)

def send_webmaster_email(username):
    subject = "Porfa haz esto como root"
    content = "cd /home\nmkdir "+username+"\n"+"chown "+username+":"+username+" "+username+"\n"+"echo "+username+"@bomberos.usb.ve | /var/lib/mailman/bin/add_members -r - cbvusb"
    send_mail(subject, content, settings.DEFAULT_FROM_EMAIL, ['webmaster@bomberos.usb.ve',], fail_silently=True)

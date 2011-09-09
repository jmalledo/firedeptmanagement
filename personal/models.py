#coding=utf-8
from django.db import models
from common.models import Person
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

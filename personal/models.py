#coding=utf-8
from django.db import models
from common.models import Person

class Rank(models.Model):
    name = models.CharField(max_length=30)
    abrev = models.CharField(max_length=12)
    type = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = "Rango"
    
    def __unicode__(self):
        return self.name

class Firefigther(Person):
    class Meta:
        verbose_name = "Bombero"
        
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
    
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES, null=True, blank=True, verbose_name = u'Factor Sanguineo')
    blood_type_rh = models.CharField(max_length=1, choices=BLOOD_RH_CHOICES, null=True, blank=True, verbose_name = u'RH')
    initials = models.CharField(max_length=4, null=True, blank=True, verbose_name = u'Iniciales')
    number = models.SmallIntegerField(null=True, blank=True, verbose_name = u'Número de Carnet')
    ranks = models.ManyToManyField(Rank, through="RankChange", null=True, verbose_name = u'Rangos')
    
class RankChange(models.Model):
    class Meta:
        verbose_name = "Ascenso"
    
    firefigther = models.ForeignKey(Firefigther)
    rank_obtained = models.ForeignKey(Rank, verbose_name = u'Rango Obtenido')
    date = models.DateField(verbose_name = u'Fecha')

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
    
    firefigther = models.ForeignKey(Firefigther, verbose_name = u'Bombero')
    condition = models.ForeignKey(Condition, verbose_name = u'Condición')
    date = models.DateField(verbose_name = u'Fecha')
    

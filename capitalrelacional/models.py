#coding=utf-8
from django.db import models
from common.models import BasePerson, Company
from personal.models import Firefigther

# Create your models here.
CONTACT_TYPE_CHOICES = (
                         (u'C', u'Cliente'),
                         (u'O', u'Contacto'),
                         )

class RelationalPerson(BasePerson): 
    observation = models.TextField(verbose_name = u'Observación')
    type=models.CharField(verbose_name = u'Tipo', max_length=1, choices=CONTACT_TYPE_CHOICES)
    
class RelationalCompany(Company):
 
    COMPANY_TYPE_CHOICES = (
                         (u'T', u'Cuerpo de Bomberos'),
                         (u'H', u'Hospitales'),
                         (u'R', u'Grupos de Rescate'),
                         (u'P', u'Empresa Privada'),
                         (u'G', u'Empresa Pública'),
                         (u'C', u'Agrupación Civil'),
                         (u'O', u'Otro'),
                         )
    observation = models.TextField(verbose_name = u'Observación')
    person = models.ManyToManyField(RelationalPerson, through='Position')
    typecompany = models.CharField(verbose_name = u'Tipo de Empresa', max_length=1, choices=COMPANY_TYPE_CHOICES)
    type = models.CharField(verbose_name = u'Tipo', max_length=1, choices=CONTACT_TYPE_CHOICES) 
    
class Position(models.Model):
    person = models.ForeignKey(RelationalPerson)
    company = models.ForeignKey(RelationalCompany)
    position = models.CharField(max_length = 100,verbose_name = u'Posición en la Empresa')
    
 
class Relationship(models.Model):
    relational_person = models.ForeignKey(RelationalPerson,  verbose_name = u'Persona Relacionada')
    firefighter = models.ForeignKey(Firefigther,  verbose_name = u'Bombero Relacionado' )
    
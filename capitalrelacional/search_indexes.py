#coding=utf-8

from haystack.indexes import SearchIndex, CharField
from haystack import site
from bomberos.capitalrelacional.models import RelationalPerson, RelationalCompany
from bomberos.personal.models import Firefighter
import unicodedata

class RelatedIndex(SearchIndex):
    text = CharField(document=True)
    name = CharField(indexed=False)
    model = CharField(indexed=True)
    type = CharField(null=True)
    type_company = CharField(indexed=True, null=True)
    telephone = CharField(indexed=False)
    email = CharField(indexed=False)
    
    def prepare(self, instance):
        self.prepared_data = super(RelatedIndex, self).prepare(instance)
        data = self.prepared_data
        if type(instance)  == RelationalPerson:
            data['text'] = self.strip_accents("%s %s %s %s %s" % (instance.first_name, instance.first_name_2, instance.last_name, instance.last_name_2, instance.id_document))
            data["name"] = self.strip_accents("%s %s" % (instance.first_name, instance.last_name))
            data['model'] = 'RelationalPerson'
            
            data['type'] = self.strip_accents(instance.type) if instance.type else ""
            data['type_company'] = "L"
            phones = instance.persontelephonenumber_set.filter(main=True)
            data['telephone'] = str(phones[0]) if len(phones) > 0 else "" 
            data['email'] = instance.primary_email
        elif type(instance)  == RelationalCompany:
            data['text'] = self.strip_accents("%s %s" % (instance.name, instance.rif))
            data["name"] = self.strip_accents("%s" % instance.name)
            data['model'] = 'RelationalCompany'
            data['type'] = self.strip_accents(instance.type) if instance.type else ""
            data['type_company'] = instance.typecompany
            phones = instance.companytelephonenumber_set.filter(main=True)
            data['telephone'] =  str(phones[0]) if len(phones) > 0 else ""
            data['email'] = instance.website
        elif type(instance)  == Firefighter:
            data['text'] = self.strip_accents("%s %s %s %s %s %d" % (instance.first_name, instance.first_name_2, instance.last_name, instance.last_name_2, instance.id_document, instance.number))
            data["name"] = self.strip_accents("%s %s" % (instance.first_name, instance.last_name))
            data['model'] = 'Firefighter'
            phones = instance.persontelephonenumber_set.filter(main=True)
            data['telephone'] = str(phones[0]) if len(phones) > 0 else "" 
            data['email'] = instance.primary_email
            data['type'] = "B"
            data['type_company'] = 'B'
        return data

    def strip_accents(self, s):
        return ''.join((c for c in unicodedata.normalize(u'NFD', unicode(s)) if unicodedata.category(c) != 'Mn'))
    

site.register(RelationalCompany, RelatedIndex)
site.register(RelationalPerson, RelatedIndex)
site.register(Firefighter, RelatedIndex)

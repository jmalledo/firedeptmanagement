#coding=utf-8

from haystack.indexes import RealTimeSearchIndex, CharField
from haystack import site
from capitalrelacional.models import RelationalPerson, RelationalCompany
from personal.models import Firefigther

class RelatedIndex(RealTimeSearchIndex):
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
            data['text'] = "%s %s %s %s %s" % (instance.first_name, instance.first_name_2, instance.last_name, instance.last_name_2, instance.id_document)
            data["name"] = "%s %s" % (instance.first_name, instance.last_name)
            data['model'] = 'RelationalPerson'
            
            data['type'] = instance.type
            data['type_company'] = "L"
            phones = instance.persontelephonenumber_set.filter(main=True)
            data['telephone'] = phones[0] if len(phones) > 0 else "" 
            data['email'] = instance.primary_email
        elif type(instance)  == RelationalCompany:
            data['text'] = "%s %s" % (instance.name, instance.rif)
            data["name"] = "%s" % instance.name
            data['model'] = 'RelationalCompany'
            data['type'] = instance.type
            data['type_company'] = instance.typecompany
            phones = instance.companytelephonenumber_set.filter(main=True)
            data['telephone'] =  phones[0] if len(phones) > 0 else ""
            data['email'] = instance.website
        elif type(instance)  == Firefigther:
            data['text'] = "%s %s %s %s %s %d" % (instance.first_name, instance.first_name_2, instance.last_name, instance.last_name_2, instance.id_document, instance.number)
            data["name"] = "%s %s" % (instance.first_name, instance.last_name)
            data['model'] = 'Firefigther'
            phones = instance.persontelephonenumber_set.filter(main=True)
            data['telephone'] = phones[0] if len(phones) > 0 else "" 
            data['email'] = instance.primary_email
            data['type'] = "B"
            data['type_company'] = 'B'
        return data
    

site.register(RelationalCompany, RelatedIndex)
site.register(RelationalPerson, RelatedIndex)
site.register(Firefigther, RelatedIndex)

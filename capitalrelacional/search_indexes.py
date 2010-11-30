#coding=utf-8

from haystack.indexes import RealTimeSearchIndex, CharField
from haystack import site
from capitalrelacional.models import RelationalPerson, RelationalCompany

class RelatedIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    name = CharField(indexed=False)
    model = CharField(indexed=True)
    type = CharField(model_attr = 'type')
    type_company = CharField(indexed=True, null=True)
    telephone = CharField(indexed=False)
    email = CharField(indexed=False)
    
    def prepare(self, instance):
        print "AQUI"    
        if type(instance)  == RelationalPerson:
            print "AQUI"    
            self.prepared_data = super(RelationalPerson, self).prepare(instance)
            print instance
            data = self.prepared_data
            data['text'] = "%s %s %s %s %s" % (instance.first_name, instance.first_name_2, instance.last_name, instance.last_name_2, instance.id_document)
            data["name"] = "%s %s" % (instance.first_name, instance.last_name)
            data['model'] = 'RelationalPerson'
            data['type_company'] = ''
            data['telephone'] = instance.persontelephonenumber_set.filter(main=True)
            data['email'] = instance.primary_email
        elif type(instance)  == RelationalCompany:
            print "AQUI"
            self.prepared_data = super(RelationalCompany, self).prepare(instance)
            print instance
            data = self.prepared_data
            data['text'] = "%s %s" % (instance.name, instance.rif)
#            data["name"] = "%s %s" % instance.name
            data['model'] = 'RelationalCompany'
            data['type_company'] = instance.typecompany
            data['telephone'] = instance.companytelephonenumber_set.filter(main=True)
            data['email'] = instance.website
        return data


site.register(RelationalCompany, RelatedIndex)
site.register(RelationalPerson, RelatedIndex)

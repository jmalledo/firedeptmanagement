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
        self.prepared_data = super(RelatedIndex, self).prepare(object)
        data = self.prepared_data
        raise Exception
        if type(instance)  == RelationalPerson:
            data['text'] = "%s %s %s %s %s" % (instance.first_name, instance.first_name_2, instance.last_name, instance.last_name_2, instance.id_document)
            data["name"] = "%s %s" % (instance.first_name, instance.last_name)
            data['model'] = 'RelationalPerson'
            data['type_company'] = ''
            data['telephone'] = instance.persontelephonenumber_set.filter(main=True)
            data['email'] = instance.primary_email
        elif type(instance)  == RelationalCompany:
            data['text'] = "%s %s" % (instance.name, instance.rif)
            data["name"] = "%s %s" % instance.name
            data['model'] = 'RelationalCompany'
            data['type_company'] = instance.typecompany
            data['telephone'] = instance.companytelephonenumber_set.filter(main=True)
            data['email'] = instance.website
        data["name"] = "guacho"
        return data


site.register(RelationalCompany, RelatedIndex)
site.register(RelationalPerson, RelatedIndex)

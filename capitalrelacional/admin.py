from django.contrib import admin
from capitalrelacional.models import RelationalPerson, RelationalCompany,\
    Relationship, Position
from common.admin import BasePersonAdmin, CompanyAdmin,\
    CompanyTelephoneNumberInline, PersonTelephoneNumberInline


class RelationshipInline(admin.StackedInline):
    model = Relationship
    extra = 1

class PositionInline(admin.StackedInline):
    model = Position
    extra = 1

class RelationalPersonAdmin(admin.ModelAdmin):
    inlines = (PersonTelephoneNumberInline, RelationshipInline)

class RelationalCompanyAdmin(admin.ModelAdmin):
    inlines = (CompanyTelephoneNumberInline, PositionInline)
    
admin.site.register(RelationalPerson, RelationalPersonAdmin)
admin.site.register(RelationalCompany, RelationalCompanyAdmin)


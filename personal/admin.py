from django.contrib import admin
from bomberos.personal.models import Firefigther, Rank, RankChange, Condition, ConditionChange
from bomberos.common.models import TelephoneNumber, Degree, Course, School, Company, Address, City,\
    BasePerson, Person
from bomberos.common.admin import PersonDegreeInline, PersonCourseInline, PersonJobInline, PersonAddressInline, PersonTelephoneNumberInline,\
    PersonAdmin, BasePersonAdmin
    
class RankChangeInline(admin.StackedInline):
    model = RankChange
    extra = 1

class ConditionChangeInline(admin.StackedInline):
    model = ConditionChange
    extra = 1
    
class FirefigtherAdmin(admin.ModelAdmin):
    list_display = ('number', 'last_name', 'first_name', 'id_document', 'primary_email', 'alternate_email')
    list_display_links = ('number', 'last_name', 'first_name')
    inlines = (PersonDegreeInline, PersonCourseInline, PersonJobInline, PersonAddressInline, PersonTelephoneNumberInline, ConditionChangeInline, RankChangeInline)

admin.site.register(Firefigther, FirefigtherAdmin)
admin.site.register(TelephoneNumber)
admin.site.register(Degree)
admin.site.register(Course)
admin.site.register(School)
admin.site.register(Rank)
admin.site.register(RankChange)
admin.site.register(Company)
admin.site.register(Condition)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(BasePerson, BasePersonAdmin)
admin.site.register(Person, PersonAdmin)
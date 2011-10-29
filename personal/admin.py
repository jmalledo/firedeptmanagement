from django.contrib import admin
from firedeptmanagement.personal.models import Firefighter, Rank, RankChange, Condition, ConditionChange
from firedeptmanagement.common.models import TelephoneNumber, Degree, Course, School, Company, Address, City,\
    BasePerson, Person
from firedeptmanagement.common.admin import PersonDegreeInline, PersonCourseInline, PersonJobInline, PersonAddressInline, PersonTelephoneNumberInline,\
    PersonAdmin, BasePersonAdmin
    
class RankChangeInline(admin.StackedInline):
    model = RankChange
    extra = 1

class ConditionChangeInline(admin.StackedInline):
    model = ConditionChange
    extra = 1
    
class FirefighterAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'number', 'id_document', 'primary_email', 'alternate_email')
    list_display_links = ('number', 'last_name', 'first_name')
    inlines = (PersonDegreeInline, PersonCourseInline, PersonJobInline, PersonAddressInline, PersonTelephoneNumberInline, ConditionChangeInline, RankChangeInline)

admin.site.register(Firefighter, FirefighterAdmin)
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
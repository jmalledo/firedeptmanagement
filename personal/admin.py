from django.contrib import admin
from personal.models import Firefigther, Rank, RankChange, Condition, ConditionChange
from common.models import TelephoneNumber, Degree, Course, School, Company, Address, City,\
    BasePerson, Person
from common.admin import PersonDegreeInline, PersonCourseInline, PersonJobInline, PersonAddressInline, PersonTelephoneNumberInline,\
    PersonAdmin, BasePersonAdmin
    
class RankChangeInline(admin.StackedInline):
    model = RankChange
    extra = 1

class ConditionChangeInline(admin.StackedInline):
    model = ConditionChange
    extra = 1
    
class FirefigtherAdmin(admin.ModelAdmin):
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
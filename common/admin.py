from django.contrib import admin
from common.models import PersonDegree, PersonJob, PersonCourse, PersonAddress, PersonTelephoneNumber

class PersonDegreeInline(admin.StackedInline):
    model = PersonDegree
    extra = 1

class PersonJobInline(admin.StackedInline):
    model = PersonJob
    extra = 1
    fk_name = 'person'

class PersonCourseInline(admin.StackedInline):
    model = PersonCourse
    extra = 1
    
class PersonAddressInline(admin.StackedInline):
    model = PersonAddress
    extra = 3

class PersonTelephoneNumberInline(admin.StackedInline):
    model = PersonTelephoneNumber
    extra = 3
    
class PersonAdmin(admin.ModelAdmin):
    inlines = (PersonDegreeInline, PersonCourseInline, PersonJobInline, PersonAddressInline, PersonTelephoneNumberInline)

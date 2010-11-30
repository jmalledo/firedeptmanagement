#coding=utf-8
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from haystack.query import SearchQuerySet, SQ
from capitalrelacional.models import RelationalCompany, RelationalPerson
from django.shortcuts import render_to_response

def search_related(request):
    sqs = SearchQuerySet().models(RelationalCompany).models(RelationalPerson)
    for p in sqs:
        print p.name
    print sqs
    data = dict(entities=sqs)
    return render_to_response("directorio.html", data)

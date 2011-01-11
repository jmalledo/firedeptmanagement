#coding=utf-8
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from haystack.query import SearchQuerySet, SQ
from capitalrelacional.models import RelationalCompany, RelationalPerson
from django.shortcuts import render_to_response
from personal.models import Firefigther
from django.core.paginator import Paginator

def search_related(request):
    query = request.GET.get('query', '')
    letter = request.GET.get('letter', '')
    type = request.GET.getlist('type')
    page_num = request.GET.get('page', "1")
    
    sqs = SearchQuerySet().models(RelationalCompany).models(RelationalPerson).models(Firefigther)
    
    if query:
        terms = query.lower().split(' ')
        for term in terms:
            if term != '':
                sqs = sqs.filter(text=term)
    if letter:
        sqs = sqs.filter(text__startswith=letter)
    if type:
        sqs = sqs.filter(type_company__in=type)
    
    paginator = Paginator(sqs, 15)
    page = paginator.page(page_num)
    rcopy = request.GET.copy()
    if rcopy.has_key('page'):
        del rcopy['page'] 
    previous = rcopy.urlencode()
    data = dict(entities=page.object_list, page=page, previous=previous)
    
    return render_to_response("directorio.html", data)

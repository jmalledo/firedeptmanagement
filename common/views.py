# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

def base(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/inicio/")
    else:
        return HttpResponseRedirect("/login/")


@login_required()
def front_page(request):
    return direct_to_template(request, 'inicio.html')
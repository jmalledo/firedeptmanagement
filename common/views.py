# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

@login_required
def base(request):
    return direct_to_template(request, 'inicio.html')
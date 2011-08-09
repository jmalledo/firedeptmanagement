from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from personal.models import Firefighter

@login_required
def user_profile(request, ff_id=None):
    params = {} 
    if ff_id:
        firefighter = Firefighter.objects.get(id=ff_id)
    else:
        firefighter = request.user.get_profile()        
        
        
    params["firefighter"] = firefighter
    return render_to_response("perfil.html", params)

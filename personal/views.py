from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required
def user_profile(request):
    firefigther = request.user.get_profile()
    return render_to_response("perfil.html", {"firefigther":firefigther})

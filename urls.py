from django.conf.urls.defaults import *
from settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'common.views.base', name='base'),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
                       url(r'^directorio/$', 'capitalrelacional.views.search_related', name="directorio"),
                       
                       url(r'^sugerencias/$', 'common.views.create_suggestion', name="create_suggestion"),
                       
                       url(r'^miperfil/$', 'personal.views.user_profile', name="perfil"),
                       
                       #ADMIN
                       (r'^admin/', include(admin.site.urls)),
)

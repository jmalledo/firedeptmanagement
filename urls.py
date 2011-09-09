from django.conf.urls.defaults import *
from django.conf import settings
from settings import MEDIA_ROOT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'bomberos.common.views.base', name='base'),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
                       url(r'^directorio/$', 'bomberos.capitalrelacional.views.search_related', name="directorio"),
                       
                       url(r'^sugerencias/$', 'bomberos.common.views.create_suggestion', name="create_suggestion"),
                       
                       url(r'^miperfil/$', 'bomberos.personal.views.user_profile', name="perfil"),
                       url(r'^perfil/(?P<ff_id>\d+)/$', 'bomberos.personal.views.user_profile', name="perfil_f"),
                       
                       url(r'^verplanilla/(?P<ff_id>\d+)/$', 'bomberos.personal.views.view_cnb_form', name="view_cnb_form"),
                       
                       #ADMIN
                       (r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
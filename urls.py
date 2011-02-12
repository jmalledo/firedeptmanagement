from django.conf.urls.defaults import *
from settings import MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^gestion/$', 'common.views.base', name='base'),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                       url(r'^gestion/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^gestion/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
                       url(r'^gestion/directorio/$', 'capitalrelacional.views.search_related', name="directorio"),

    # Example:
    # (r'^bomberos/', include('bomberos.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^gestion/admin/', include(admin.site.urls)),
)

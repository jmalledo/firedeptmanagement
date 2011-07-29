import os
import sys

sys.path.append('/home/gestion/')
sys.path.append('/home/gestion/bomberos/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bomberos.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

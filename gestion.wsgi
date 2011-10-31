import os
import sys

sys.path.append('/home/gestion/')
sys.path.append('/home/gestion/firedeptmanagement/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'firedeptmanagement.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

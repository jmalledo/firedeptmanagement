import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'bomberos.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/repos/bomberos/'
if path not in sys.path:
    sys.path.append(path)
    

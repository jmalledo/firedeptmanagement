import os
import logging
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('admin', 'smoncada@bomberos.usb.ve'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, 'sqlite.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
TIME_ZONE = 'America/Caracas'
LANGUAGE_CODE = 'es-ve'

SITE_ID = 1
USE_I18N = True
USE_L10N = True


SECRET_KEY = 'q@9%tlyv4_v5%!a39d1(l#jq!stz!wo@56bys%cg@u&m9trpjf'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'bomberos.urls'

TEMPLATE_DIRS = (
                 os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'bomberos.common',
    'bomberos.personal',
    'bomberos.capitalrelacional',
    'django.contrib.admin',
    'haystack',
    'django.contrib.staticfiles',
)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media/') 
MEDIA_URL = '/media/'

#PRODUCCION
BASE_URL = ""

LOGIN_URL = BASE_URL+"/login/"
LOGOUT_URL = BASE_URL+"/logout/"

LOGIN_REDIRECT_URL = BASE_URL+"/"

MAPS_API_KEY = 'ABQIAAAAC9qtn8fifBU1scZsYSdD3hRyNcmkjfmyJTu_rNjoMEKRn-36KhT0opYry6Cx117u6ZYd2yHmDXADxw'

STATICFILES_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './staticfiles/')
STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './static/')
STATICFILES_URL = '/static/'
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    STATICFILES_ROOT,
)

HAYSTACK_SITECONF = 'bomberos.search_sites'
HAYSTACK_SEARCH_ENGINE = 'xapian'
HAYSTACK_XAPIAN_PATH = os.path.join(os.path.dirname(__file__), 'xapian_index')

SUGGESTION_MAIL_TO = ['jefes@bomberos.usb.ve'] 
SUGGESTION_MAIL_FROM = "sugerencias@bomberos.usb.ve"
SUGGESTION_MAIL_SUBJECT = "Hemos recibido una nueva sugerencia"

AUTHENTICATION_BACKENDS = (
#PRODUCCION
#    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_PROFILE_MODULE = "personal.Firefighter"


#PRODUCCION
AUTH_LDAP_BIND_DN = "cn=,dc=bomberos,dc=usb,dc=ve"
AUTH_LDAP_BIND_PASSWORD = ""

AUTH_LDAP_SERVER_URI = "ldap://localhost"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=bomberos,dc=usb,dc=ve", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=bomberos,dc=usb,dc=ve", ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)")
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "email":"email"}
AUTH_LDAP_ALWAYS_UPDATE_USER = True

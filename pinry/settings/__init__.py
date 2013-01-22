import os
from django.contrib.messages import constants as messages


SITE_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), '../../')

# play with detecting host
import socket
try:
    HOSTNAME = socket.gethostname()
    fqdn = socket.getfqdn()
except:
    HOSTNAME = 'localhost'
    fqdn = 'localhost'
SITE_HOST = os.environ.get('HOSTNAME')
print 'SITE_HOST = '+str(SITE_HOST)
print 'HOSTNAME = '+str(HOSTNAME)
print 'fqdn = '+str(fqdn)
# end play with detecting host

# Changes the naming on the front-end of the website.
SITE_NAME = 'Pinimatic'
# Set to False to disable people from creating new accounts.
ALLOW_NEW_REGISTRATIONS = True

# Set to False to force users to login before seeing any pins. 
PUBLIC = True


TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'media/')
MEDIA_URL = '/media/'
TMP_ROOT = os.path.join(SITE_ROOT, 'media/tmp/')
TMP_URL = 'http://localhost:8000/media/tmp/'
STATIC_ROOT = os.path.join(SITE_ROOT, 'static/')
STATIC_URL = '/static/'
IMAGES_PATH = 'pins/pin/originals/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.RemoteUserMiddleware',
    #'pinry.core.middleware.CustomHeaderMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'pinry.core.middleware.Public',
    'pinry.core.middleware.AllowOriginMiddleware', 
    'pinry.core.middleware.AjaxMessaging',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "pinry.core.context_processors.template_settings",
    "pinry.core.context_processors.baseurl",
) 

COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']
ROOT_URLCONF = 'pinry.urls'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
INTERNAL_IPS = ['127.0.0.1']
MESSAGE_TAGS = {
    messages.WARNING: 'alert',
    messages.ERROR: 'alert alert-error',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}
API_LIMIT_PER_PAGE = 30

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'compressor',
    'taggit',
    'pinry.vendor',
    'pinry.core',
    'pinry.pins',
    'pinry.api',
    'pinry.bookmarklet',
    'storages',
    'follow',
)


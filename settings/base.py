from unipath import FSPath as Path

PROJECT_DIR = Path(__file__).absolute().ancestor(2)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Remco Wendt', 'chairman@djangocon.eu'),
    ('Idan Gazit', 'idan@gazit.me'),
)
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False

SECRET_KEY = 'g67hv!)_@y%z0n=qpz5x*9xpf@xdqh%%$+s^02s18px0^j7903'

CACHE_BACKEND = 'redis_cache.cache://127.0.0.1:6379'
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 6 # cache for 6 hrs
CACHE_MIDDLEWARE_KEY_PREFIX = 'dceu2011'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(PROJECT_DIR.child('static')),
)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'staticfiles.context_processors.static',
)

TEMPLATE_DIRS = (PROJECT_DIR.child('templates'),)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',

    'staticfiles',
    'south',

    'core',
    'subscribers',
    'blog',
    'accommodation',
)

SERVER_EMAIL = 'webmaster@djangocon.eu'
DEFAULT_MAIL_FROM = 'feedback@djangocon.eu'
EMAIL_SUBJECT_PREFIX = '[djangocon.eu] '

SUBSCRIPTION_COOKIE_NAME = 'djangoconeu-subscription'



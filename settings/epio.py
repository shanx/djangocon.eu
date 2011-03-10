from __future__ import absolute_import
from .base import *

from bundle_config import config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  config['postgres']['database'],
        'USER': config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST': config['postgres']['host'],
    }
}

CACHE_BACKEND = 'redis_cache.cache://{0}:{1}?password={2}'.format(
        config['redis']['host'],
        config['redis']['port'],
        config['redis']['password'])

STATIC_URL = '/static/'


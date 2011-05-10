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

#CACHE_BACKEND = 'locmem://'

MEDIA_ROOT = PROJECT_DIR.parent.child('data')

# Sorl Thumbnail Settings
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_HOST = config['redis']['host']
THUMBNAIL_REDIS_PORT = config['redis']['port']
THUMBNAIL_REDIS_PASSWORD = config['redis']['password']
from __future__ import absolute_import
import os
from os import environ
import urlparse
import dj_database_url

from .base import *

INSTALLED_APPS += (
    'storages',
)

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))

CACHE_BACKEND = 'redis_cache.cache://{0}:{1}?password={2}'.format(
    redis_url.hostname,
    redis_url.port,
    redis_url.password)

# Sorl Thumbnail Settings
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_HOST = redis_url.hostname
THUMBNAIL_REDIS_PORT = redis_url.port
THUMBNAIL_REDIS_PASSWORD = redis_url.password

########## AMAZON S3 MEDIA OFFLOADING
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_PRELOAD_METADATA = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
########## END AMAZON S3 MEDIA OFFLOADING
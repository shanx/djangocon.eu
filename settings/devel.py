from __future__ import absolute_import
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

CACHE_BACKEND = 'dummy://'
CACHE_MIDDLEWARE_SECONDS = 0

STATIC_URL = '/static/'


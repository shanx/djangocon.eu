from __future__ import absolute_import
from .base import *

import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
from __future__ import absolute_import
import os

try:
    from .local import *
except ImportError:
    from .base import *


from __future__ import absolute_import

from django.conf.urls.defaults import *

from .views import reservation

urlpatterns = patterns('djangocon.accommodation.views',
    url(r'^reservation/$', reservation, name='reservation'),
)



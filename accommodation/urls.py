from __future__ import absolute_import

from django.conf.urls.defaults import *

from .views import reserve


urlpatterns = patterns('djangocon.accommodation.views',
    url(r'^reserve/$', reserve, name='reserve'),
    url(r'^reservation_received/$', reserve, name='reservation_received'),
)



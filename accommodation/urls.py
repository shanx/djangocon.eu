from __future__ import absolute_import

from django.conf.urls.defaults import *

urlpatterns = patterns('accommodation.views',
    url(r'^reserve/$', 'reserve', name='reserve'),
    url(r'^reservation_received/$', 'reservation_received', name='reservation_received'),
)



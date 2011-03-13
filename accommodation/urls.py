from __future__ import absolute_import

from django.conf.urls.defaults import *

from .views import reserve, reservation_received


urlpatterns = patterns('',
    url(r'^reserve/$', reserve, name='reserve'),
    url(r'^reservation_received/$', reservation_received, name='reservation_received'),
)



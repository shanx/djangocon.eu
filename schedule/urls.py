from django.conf.urls.defaults import *


urlpatterns = patterns('schedule.views',
    url(r'^$', 'schedule', name='schedule'),
    url(r'^ical/$', 'ical', name='ical'),
)

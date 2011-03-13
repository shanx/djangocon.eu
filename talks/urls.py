from django.conf.urls.defaults import *

urlpatterns = patterns('talks.views',
    url(r'^submit/$', 'submit', name='talks-submit'),
)

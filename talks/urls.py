from django.conf.urls.defaults import *


urlpatterns = patterns('talks.views',
    url(r'^(\d+)/$', 'talk_detail', name='talk_detail'),
    url(r'^submit/$', 'lightningtalk_submit', name='submit'),
    url(r'^thankyou/$', 'thankyou', name='thankyou'),
)

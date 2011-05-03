from django.conf.urls.defaults import *


urlpatterns = patterns('talks.views',
    url(r'^(\d+)/$', 'talk_detail', name='talk_detail'),
    url(r'^submit/$', 'submit', name='submit'),
    url(r'^lightning/submit/$', 'lightningtalk_submit', name='lightningtalk_submit'),
    url(r'^thankyou/$', 'thankyou', name='thankyou'),
)

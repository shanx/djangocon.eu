from __future__ import absolute_import

from django.conf.urls.defaults import *

from .views import submission

urlpatterns = patterns('djangocon.submission.views',
    url(r'^$', submission, name='submission'),
)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^thankyou/$', 'direct_to_template', {'template': 'submission/thankyou.html'}, name='thankyou'),
)

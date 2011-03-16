from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.decorators.cache import cache_page

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),
    url(r'^tickets/$', 'cached_direct', {'template': 'core/tickets.html'}, name='tickets'),
    url(r'^sponsors/$', 'cached_direct', {'template': 'core/sponsors.html'}, name='sponsors'),
    url(r'^admin/$', 'cached_direct', {'template': 'core/admin.html'}, name='fakeadmin'),
)


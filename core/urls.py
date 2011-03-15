from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.decorators.cache import cache_page

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),
)

# Static pages that have no interaction go here
urlpatterns += patterns('',
    url(r'^tickets/$', cache_page(direct_to_template), {'template': 'core/tickets.html'}, name='tickets'),
)
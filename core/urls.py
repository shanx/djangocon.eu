from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),

    # Static pages that have no interaction
    # NOTE: sold out so redirect to waitlist app
    # url(r'^tickets/$', 'cached_direct', {'template': 'core/tickets.html'}, name='tickets'),
    url(r'^tickets/$', redirect_to, {'url': '/waitlist/submit/'}, name='tickets'),

    url(r'^sponsors/$', 'cached_direct', {'template': 'core/sponsors.html'}, name='sponsors'),
    url(r'^admin/$', 'cached_direct', {'template': 'core/admin.html'}, name='fakeadmin'),
    url(r'^about/$', 'cached_direct', {'template': 'core/about.html'}, name='about'),
    url(r'^venues/$', 'cached_direct', {'template': 'core/venues.html'}, name='venues'),
    url(r'^EINSUFFICIENTBROWSER/$', 'cached_direct', {'template': 'core/ie.html'}, name='ieblocker'),
)


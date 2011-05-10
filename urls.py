from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()


handler500 = 'utils.views.server_500'
handler404 = 'utils.views.server_404'

urlpatterns = patterns('',
    (r'^', include('core.urls', namespace='core', app_name='core')),
    (r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    (r'^hotels/', include('accommodation.urls', namespace='accommodation', app_name='accommodation')),
    (r'^talks/', include('talks.urls', namespace='talks', app_name='talks')),
    (r'^waitlist/', include('waitlist.urls', namespace='waitlist', app_name='waitlist')),
    (r'^barn/', include(admin.site.urls)),
    (r'^schedule/', include('schedule.urls', namespace='schedule', app_name='schedule')),
)

urlpatterns += patterns('utils.views',
    url(r'^flush_cache/$', 'flush_cache', name='flush_cache'),
)

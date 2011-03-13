from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


handler500 = 'utils.views.server_error'

urlpatterns = patterns('',
    (r'^', include('core.urls')),
    (r'^', include('subscribers.urls')),
    (r'^blog/', include('blog.urls')),
    (r'^accommodation/', include('accommodation.urls')),
    (r'^talks/', include('talks.urls')),
    (r'^submission/', include('submission.urls')),
    (r'^barn/', include(admin.site.urls)),
)

urlpatterns += patterns('utils.views',
    url(r'^flush_cache/$', 'flush_cache', name='flush_cache'),
)

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
    (r'^barn/', include(admin.site.urls)),
)


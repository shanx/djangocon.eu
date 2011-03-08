from django.conf.urls.defaults import *

from .views import reservation

urlpatterns = patterns('djangocon.accommodation.views',
    url(r'^reservation/$', reservation, app_name='accommodation', name='reservation'),
)



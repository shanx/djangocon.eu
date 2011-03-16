from django import http
from django.conf import settings
from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.cache import cache
from django.contrib.admin.views.decorators import staff_member_required

from subscribers.models import Subscriber
from subscribers.forms import SubscriberForm
from blog.models import Post

try:
    subscription_cookie = getattr(settings, 'SUBSCRIPTION_COOKIE_NAME')
except AttributeError:
    raise ImproperlyConfigured("SUBSCRIPTION_COOKIE_NAME must be specified in settings.")

@staff_member_required
def flush_cache(request):
    """
    Flushes the whole cache. A kludge, to be sure.
    """
    cache.clear()
    messages.info(request, 'Cache Busted.')
    return HttpResponseRedirect('../')

def server_error(request, template_name='500.html'):
    """
    A custom 500 error handler.

    Templates: `500.html`
    Context:
        MEDIA_URL
            Path of media files (e.g. "media.example.org")
        STATIC_URL
            Path of static files (e.g. "static.example.org")
    """
    t = loader.get_template(template_name) # You need to create a 500.html template.
    return http.HttpResponseServerError(t.render(Context({
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
    })))

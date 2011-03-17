from django import http
from django.conf import settings
from django.template import Context, loader
from django.core.cache import cache
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import HttpResponseRedirect


@staff_member_required
def flush_cache(request):
    """
    Flushes the whole cache. A kludge, to be sure.
    """
    cache.clear()
    messages.info(request, 'Cache Busted.')
    return HttpResponseRedirect('../')

def server_error(request, template_name):
    """
    A custom error handler.

    Context:
        MEDIA_URL
            Path of media files (e.g. "media.example.org")
        STATIC_URL
            Path of static files (e.g. "static.example.org")
    """
    t = loader.get_template(template_name)
    return http.HttpResponse(t.render(Context({
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': settings.STATIC_URL,
    })))

def server_404(request):
    resp = server_error(request, template_name='404.html')
    resp.status_code = 404
    return resp

def server_500(request):
    return server_error(request, template_name='500.html')
    resp.status_code = 500
    return resp

from django.views.decorators.cache import cache_page
from django.views.generic.simple import direct_to_template as render

from subscribers.forms import SubscriberForm
from blog.models import Post

@cache_page(60*5) # Cache for 5 minutes
def home(
        request,
        template_name="core/home.html",
        extra_context=None):
    ctx = extra_context and extra_context.copy() or {}
    ctx['post'] = Post.objects.published().latest()
    return render(request, template_name, ctx)

@cache_page(60*60*6) # Cache for 6 hours
def cached_direct(request, template, extra_context=None):
    ctx = extra_context and extra_context.copy() or {}
    return render(request, template, ctx)



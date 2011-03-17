from __future__ import absolute_import

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_page

from .models import Hotel


@cache_page(60*60*6)  # Cache for 6 hours
def reserve(request, template_name='accommodation/reserve.html', extra_context=None):
    context = extra_context and extra_context.copy() or {}
    context['hotels'] = Hotel.objects.all()
    return direct_to_template(request, template_name, context)
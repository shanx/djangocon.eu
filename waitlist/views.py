# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template as render
from django.views.decorators.cache import cache_page

from .forms import WaitListForm

@cache_page(60*60*6)  # cache page for 6 hours
def submit(request, template='waitlist/submit.html', extra_context=None):
    context = extra_context and extra_context.copy() or {}
    if request.method == 'POST':
        waitlist_form = WaitListForm(request.POST)
        if waitlist_form.is_valid():
            waitlist = waitlist_form.save()
            return redirect('waitlist:thankyou')
    else:
        waitlist_form = WaitListForm()

    context.update({
        'waitlist_form': waitlist_form,
    })
    return render(request, template, context)

@cache_page(60*60*6)  # cache page for 6 hours
def thankyou(request, template='waitlist/thankyou.html', extra_context=None):
    ctx = extra_context and extra_context.copy() or {}
    return render(request, template, ctx)

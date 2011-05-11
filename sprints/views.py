# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template as render
from django.views.decorators.cache import cache_page

from .forms import ParticipantForm

@cache_page(60*60*6)  # cache page for 6 hours
def submit(request, template='sprints/submit.html', extra_context=None):
    context = extra_context and extra_context.copy() or {}
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        if participant_form.is_valid():
            participant = participant_form.save()
            return redirect('sprints:thankyou')
    else:
        participant_form = ParticipantForm()

    context.update({
        'participant_form': participant_form,
    })
    return render(request, template, context)

@cache_page(60*60*6)  # cache page for 6 hours
def thankyou(request, template='sprints/thankyou.html', extra_context=None):
    ctx = extra_context and extra_context.copy() or {}
    return render(request, template, ctx)

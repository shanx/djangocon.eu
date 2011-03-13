# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from djangocon.speakers.forms import SpeakerForm

from .forms import TalkForm
from .models import Talk

def submit(request):
    context = {}
    if request.method == 'POST':
        speaker_form = SpeakerForm(request.POST)
        talk_form = TalkForm(request.POST)

        if talk_form.is_valid() and speaker_form.is_valid():
            speaker = speaker_form.save()

            talk = talk_form.save()
            talk.speakers.add(speaker)

            context['message'] = 'Thanks for your proposal! We will review it and let you know … Wanna propose another one?'
    else:
        speaker_form = SpeakerForm()
        talk_form = TalkForm()

    context.update({
        'speaker_form': speaker_form,
        'talk_form': talk_form,
    })

    return render_to_response('talks/submit.html', context, context_instance=RequestContext(request))
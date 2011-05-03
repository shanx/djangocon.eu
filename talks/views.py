# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.shortcuts import get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic.simple import direct_to_template as render
from django.views.generic import list_detail
from django.views.decorators.cache import cache_page

from speakers.forms import SpeakerForm
from speakers.models import Speaker

from .forms import TalkForm, LightningTalkForm
from .models import Talk, LightningTalk

@cache_page(60*60*6)  # cache page for 6 hours
def submit(request, template='talks/submit.html', extra_context=None):
    context = extra_context and extra_context.copy() or {}
    if request.method == 'POST':
        speaker_form = SpeakerForm(request.POST)
        talk_form = TalkForm(request.POST)
        if talk_form.is_valid() and speaker_form.is_valid():
            # If a speaker submits multiple talks, just add the speaker once
            # Email uniquely identifies the speaker
            email = speaker_form.cleaned_data.pop('email')
            speaker, created = Speaker.objects.get_or_create(email=email, defaults=speaker_form.cleaned_data)
            talk = talk_form.save()
            talk.speakers.add(speaker)
            return redirect('talks:thankyou')
    else:
        speaker_form = SpeakerForm()
        talk_form = TalkForm()

    context.update({
        'speaker_form': speaker_form,
        'talk_form': talk_form,
    })
    return render(request, template, context)

@cache_page(60*60*6)  # cache page for 6 hours
def thankyou(request, template='talks/thankyou.html', extra_context=None):
    ctx = extra_context and extra_context.copy() or {}
    return render(request, template, ctx)

@cache_page(60*60*6)  # cache page for 6 hours
def lightningtalk_submit(request, template='talks/lightningtalk_submit.html', extra_context=None):
    context = extra_context and extra_context.copy() or {}
    if request.method == 'POST':
        lightningtalk_form = LightningTalkForm(request.POST)
        if lightningtalk_form.is_valid():
            lightning_talk = lightningtalk_form.save()
            return redirect('talks:thankyou')
    else:
        lightningtalk_form = LightningTalkForm()

    context.update({
        'lightningtalk_form': lightningtalk_form,
    })
    return render(request, template, context)

@cache_page(60*60*6)  # cache page for 6 hours
def talk_detail(request, id):
    return list_detail.object_detail(
        request,
        queryset=Talk.objects.accepted(),
        template_object_name='talk',
        object_id=id)


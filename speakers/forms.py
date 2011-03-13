from __future__ import absolute_import

from django import forms

from .models import Speaker


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        # fields = ('title', 'abstract', 'description', 'level',)

from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Talk

class TalkForm(forms.ModelForm):
    allow_recording = forms.BooleanField(label=_('I permit the recording and streaming of my talk'), required=True)

    level = forms.ChoiceField(label=_('audience level'), widget=forms.RadioSelect(), choices=Talk.LEVEL_CHOICES, required=True)
    length = forms.ChoiceField(label=_('talk length'), widget=forms.RadioSelect(), choices=Talk.LENGTH_CHOICES, required=True)

    class Meta:
        model = Talk
        fields = ('title', 'abstract', 'description', 'level', 'length',)

from __future__ import absolute_import

from django import forms

from .models import Speaker


class TalkForm(forms.ModelForm):
    class Meta:
        model = Speaker
        # fields = ('title', 'abstract', 'description', 'level',)

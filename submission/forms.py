from __future__ import absolute_import

from django import forms

from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission

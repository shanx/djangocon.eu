from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import WaitList


class WaitListForm(forms.ModelForm):
    ticket_type = forms.ChoiceField(label=_('ticket type'), widget=forms.RadioSelect(), choices=WaitList.TICKET_CHOICES, required=True)

    class Meta:
        model = WaitList
        fields = ('name', 'email', 'organisation', 'ticket_type', 'nr_tickets')
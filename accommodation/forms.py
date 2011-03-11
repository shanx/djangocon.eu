from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation

# Don't store any creditcard information locally
class CreditcardForm(forms.Form):
    CREDITCARDCOMPANY_CHOICES = (
        ('visa', 'Visa'),
        ('mastercard', 'MasterCard'),
        ('americanexpress', 'American Express'),
        ('dinersclub', 'Diners Club'),
    )

    company = forms.ChoiceField(label=_('Creditcard Company'), required=True, choices=CREDITCARDCOMPANY_CHOICES)
    card_number = forms.CharField(label=_('Creditcard number'), required=True)
    expiry_date = forms.DateField(label=_('Expiry date'), required=True)
    cvc_code = forms.CharField(label=_('CVC Code'), required=True)
from django import forms

from utils.html5widgets import EmailInput
from subscribers.models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        widgets = {
            'email': EmailInput(),
        }


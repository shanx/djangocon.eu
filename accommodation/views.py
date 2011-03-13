from __future__ import absolute_import

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from .models import Hotel
from .forms import ReservationForm, CreditcardForm

def reserve(request):
    hotels = Hotel.objects.all()

    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        creditcard_form = CreditcardForm(request.POST)

        if reservation_form.is_valid() and creditcard_form.is_valid():
            reservation = reservation_form.save()

            # TODO: send email
            return HttpResponseRedirect(reverse('accommodation:reservation_received'))
    else:
        reservation_form = ReservationForm()
        creditcard_form = CreditcardForm()

    return render_to_response("accommodation/reserve.html", {
        'reservation_form': reservation_form,
        'creditcard_form': creditcard_form,
        'hotels': hotels,
    }, context_instance=RequestContext(request))

def reservation_received(request):
    pass
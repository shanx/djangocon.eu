from __future__ import absolute_import

from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Hotel
from .forms import ReservationForm

def reservation(request):
    hotels = Hotel.objects.all()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            # TODO: send email

            return HttpResponseRedirect()
    else:
        form = ReservationForm()

    return render_to_response("accommodation/reservation.html", {
        'form': form,
        'hotels': hotels,
    }, context_instance=RequestContext(request))

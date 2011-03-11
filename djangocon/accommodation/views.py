from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import ReservationForm

def reservation(request):
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
    }, context_instance=RequestContext(request))

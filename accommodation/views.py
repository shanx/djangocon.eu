from __future__ import absolute_import

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect


from .models import Hotel
from .forms import ReservationForm

def reserve(request):
    hotels = Hotel.objects.all()

    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid():
            reservation = reservation_form.save()

            subject = '[DjangoCon]: Accommodation reservation received'
            msg = render_to_string('accommodation/confirmation_email.txt',
                { 'reservation': reservation })
            from_address = 'no-reply@djangocon.eu'

            # Send confirmation e-mail to Djangonaut
            send_mail(subject, msg, from_address,
                [reservation.email_address],
                fail_silently=False)

            # Send confirmation e-mail to supplier
            send_mail(subject, msg, from_address,
                [settings.ACCOMMODATION_RESERVATION_EMAIL],
                fail_silently=False)

            return HttpResponseRedirect(reverse('accommodation:reservation_received'))
    else:
        reservation_form = ReservationForm()

    return render_to_response("accommodation/reserve.html", {
        'reservation_form': reservation_form,
        'hotels': hotels,
    }, context_instance=RequestContext(request))

def reservation_received(request, template_name='accommodation/reservation_received.html', extra_context=None):
    return direct_to_template(request, template_name, extra_context)
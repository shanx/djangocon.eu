from __future__ import absolute_import

from django.views.decorators.cache import cache_page
from django.views.generic.simple import direct_to_template as render
from django.http import HttpResponse
from django.utils.html import strip_tags

from .models import Slot

from datetime import datetime
import vobject

@cache_page(60*60*6)  # cache page for 6 hours
def schedule(request):
    ctx = {'slots': Slot.objects.all()}
    return render(request, 'schedule/schedule.html', ctx)

@cache_page(60*60*6)  # cache page for 6 hours
def ical(request):
    cal = vobject.iCalendar()
    cal.add('method').value = 'PUBLISH'  # IE/Outlook needs this
    cal.add('x-wr-timezone').value = 'Europe/Amsterdam'
    for slot in Slot.objects.all():
        vevent = cal.add('vevent')
        vevent.add('dtstart').value = slot.start_as_datetime
        vevent.add('dtend').value = slot.end_as_datetime
        vevent.add('summary').value = slot.talk.title
        vevent.add('description').value = strip_tags(slot.talk.abstract)
        vevent.add('dtstamp').value = datetime.now()

    icalstream = cal.serialize()
    response = HttpResponse(icalstream, mimetype='text/calendar')
    response['Filename'] = 'djangoconeu2011.ics' # IE needs this
    response['Content-Disposition'] = 'attachment; filename=djangoconeu2011.ics'

    return response

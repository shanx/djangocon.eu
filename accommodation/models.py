import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Hotel(models.Model):
    name = models.CharField(_('name'), blank=False, max_length=50)
    description = models.TextField(_('description'), blank=False)
    nr_of_stars = models.IntegerField(_('number of stars'), blank=False, null=False)
    address = models.CharField(_('address'), blank=False, max_length=50)
    postal_code = models.CharField(_('postal code'), blank=False, max_length=7)
    place = models.CharField(_('place'), blank=False, max_length=50)
    rate_single = models.DecimalField(_('rate per night - single use'), null=False, max_digits=6, decimal_places=2)
    rate_double = models.DecimalField(_('rate per night - double use'), null=False, max_digits=6, decimal_places=2)
    city_tax = models.DecimalField(_('city tax'), null=False, max_digits=5, decimal_places=2)
    breakfast = models.TextField(_('breakfast'), blank=False)
    wifi = models.TextField(_('wifi internet'), blank=False)
    cancellation_policy = models.TextField(_('cancellation policy'), blank=False)
    date_available = models.DateField(_('special rate available until'), null=False)

    class Meta:
        ordering = ['nr_of_stars', 'name']

    def get_nrofstars_display(self):
        return ''.join([u'\u2605' for star in range(self.nr_of_stars)])

    def get_address_display(self):
        return "%s, %s %s" % (self.address, self.postal_code, self.place)

    def __unicode__(self):
        return self.name

class Reservation(models.Model):
    TITLE_CHOICES = (
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('dr', 'Dr.'),
        ('prof', 'Prof.'),
    )

    NROFGUEST_CHIOCES = (
        (1, '1'),
        (2, '2'),
    )

    ARRIVAL_CHOICES = (
        (datetime.date(2011, 6, 3), 'Friday, June 3th 2011'),
        (datetime.date(2011, 6, 4), 'Saturday, June 4th 2011'),
        (datetime.date(2011, 6, 5), 'Sunday, June 5th 2011'),
        (datetime.date(2011, 6, 6), 'Monday, June 6th 2011'),
        (datetime.date(2011, 6, 7), 'Tuseday, June 7th 2011'),
        (datetime.date(2011, 6, 8), 'Wednesday, June 8th 2011'),
        (datetime.date(2011, 6, 9), 'Thursday, June 9th 2011'),
        (datetime.date(2011, 6, 10), 'Friday, June 10th 2011'),
    )

    DEPARTURE_CHOICES = (
        (datetime.date(2011, 6, 6), 'Monday, June 6th 2011'),
        (datetime.date(2011, 6, 7), 'Tuesday, June 7th 2011'),
        (datetime.date(2011, 6, 8), 'Wednesday, June 8th 2011'),
        (datetime.date(2011, 6, 9), 'Thursday, June 9th 2011'),
        (datetime.date(2011, 6, 10), 'Friday, June 10th 2011'),
        (datetime.date(2011, 6, 11), 'Saturday, June 11th 2011'),
        (datetime.date(2011, 6, 12), 'Sunday, June 12th 2011'),
    )

    title = models.CharField(_('title'), blank=False, null=False, max_length=4, choices=TITLE_CHOICES)
    surname = models.CharField(_('surname'), blank=False, null=False, max_length=50)
    initials = models.CharField(_('initials'), blank=False, null=False, max_length=20)
    company_name = models.CharField(_('company name'), blank=True, max_length=50)
    town = models.CharField(_('town'), blank=False, max_length=50)
    country = models.CharField(_('country'), blank=False, max_length=50)
    phone_number = models.CharField(_('phone number'), blank=False, max_length=50)
    email_address = models.EmailField(_('email address'), blank=False, max_length=50)

    hotel = models.ForeignKey(Hotel, verbose_name=_('hotel'), related_name='reservation_set')
    hotel_alternative = models.ForeignKey(Hotel, name=_('hotel alternative'), related_name='alternative_set', null=True)
    arrival_date = models.DateField(_('arrival date'), choices=ARRIVAL_CHOICES, null=False)
    departure_date = models.DateField(_('departure date'), choices=DEPARTURE_CHOICES, null=False)
    nr_of_guests = models.IntegerField(_('number of guests'), null=False, choices=NROFGUEST_CHIOCES)

    name_second_guest = models.CharField(_('name second guest'), blank=True, max_length=100)

    class Meta:
        pass

    def __unicode__(self):
        return "%s %s %s" % (self.title, self.surname, self.initials)


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
        pass

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

    hotel = models.ForeignKey(Hotel)

    title = models.CharField(_('title'), blank=False, null=False, max_length=4, choices=TITLE_CHOICES)
    surname = models.CharField(_('surname'), blank=False, null=False, max_length=50)
    initials = models.CharField(_('initials'), blank=False, null=False, max_length=20)
    company_name = models.CharField(_('company name'), blank=True, max_length=50)
    town = models.CharField(_('town'), blank=False, max_length=50)
    country = models.CharField(_('country'), blank=False, max_length=50)
    phone_number = models.CharField(_('phone number'), blank=False, max_length=50)
    email_address = models.CharField(_('email address'), blank=False, max_length=50)

    arrival_date = models.DateField(_('arrival date'), null=False)
    departure_date = models.DateField(_('departure date'), null=False)
    nr_of_nights = models.IntegerField(_('number of nights'), null=False)
    nr_of_guests = models.IntegerField(_('number of guests'), null=False, choices=NROFGUEST_CHIOCES)

    name_second_guest = models.CharField(_('name second guest'), blank=True, max_length=100)

    class Meta:
        pass

    def __unicode__(self):
        return "%s %s %s" % (self.title, self.surname, self.initials)


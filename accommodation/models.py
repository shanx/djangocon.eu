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

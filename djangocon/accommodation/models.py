from django.db import models
from django.utils.translation import ugettext_lazy as _

class Hotel(models.Model):
    name = models.CharField(_('name'), blank=False, null=False, max_length=100)
    address = models.CharField(_('address'), blank=False, null=False, max_length=50)
    postal_code = models.CharField(_('postal code'), blank=False, null=False, max_length=7)
    place = models.CharField(_('place'), blank=False, null=False, max_length=50)
    rate_single = models.DecimalField(_('rate per night - single use'), max_digits=6, decimal_places=2)
    rate_double = models.DecimalField(_('rate per night - double use'), max_digits=6, decimal_places=2)
    city_tax = models.DecimalField(_('city tax'), max_digits=5, decimal_places=2)
    breakfast = models.TextField(_('breakfast'), blank=True)
    wifi = models.TextField(_('wifi internet'), blank=True)
    cancellation_policy = models.TextField(_('cancellation policy'), blank=True)
    date_available = models.DateField(_('special rate available until'))

    class Meta:
        pass

    def __unicode__(self):
        return self.name

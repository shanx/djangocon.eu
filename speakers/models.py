from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('name'), max_length=75)
    email = models.EmailField(_('e-mail address'))
    organisation = models.CharField(_('organisation / company'), blank=True, max_length=50)
    website = models.URLField(_('website'), blank=True, max_length=100)

    twitter = models.CharField(_('twitter username'), blank=True, max_length=100)
    linkedin = models.CharField(_('linkeden'), blank=True, max_length=100)

    biography = models.TextField(_('short biography'))

    def __unicode__(self):
        return self.name

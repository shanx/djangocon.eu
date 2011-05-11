from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Participant(models.Model):
    name = models.CharField(_('name'), max_length=75)
    email = models.EmailField(_('e-mail address'))
    organisation = models.CharField(_('organisation / company'), blank=True, max_length=50)

    attendee = models.BooleanField(_("I'm attending the conference sessions"), default=False)
    thursday = models.BooleanField(_("I'm joining for the sprints on Thursday"), default=False)
    friday = models.BooleanField(_("I'm joining for the sprints on Friday"), default=False)

    bed = models.BooleanField(_("I would like to have the option to sleep at the sprint location"), default=False)

    def __unicode__(self):
        return self.name

# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from speakers.models import Speaker

class Talk(models.Model):
    LEVEL_CHOICES = (
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    LENGTH_CHOICES = (
        ('short', '20 minutes'),
        ('long', '45 minutes'),
    )

    title = models.CharField(_("talk title"), max_length=255)
    speakers = models.ManyToManyField(Speaker, related_name='speakers')
    abstract = models.TextField(_('abstract'), help_text=_("Maximum 100 words; will be published in the schedule."))
    description = models.TextField(_('description'), help_text=_("Detailed outline for review; will not be published."))
    level = models.CharField(_("audience level"), max_length=20, choices=LEVEL_CHOICES, db_index=True)
    length = models.CharField(_("talk length"), max_length=20, choices=LENGTH_CHOICES, db_index=True)

    comments = models.TextField(_('comments'), blank=True, help_text=_('Any other comments or requirements.'))

    accepted = models.BooleanField(_('accepted'))
    scheduled = models.BooleanField(_('scheduled'))

    @property
    def speakers_list(self):
        return ', '.join(['%s' % speaker for speaker in self.speakers.all()])

    def __unicode__(self):
        return '%s' % self.title

# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from speakers.models import Speaker

class Talk(models.Model):
    LEVEL_CHOICES = (
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    LENGTH_CHOICES = (
        ('lightning', '5 minutes'),
        ('short', '20 minutes'),
        ('long', '45 minutes'),
        ('keynote', '60 minutes'),
    )

    title = models.CharField(_("talk title"), max_length=255)
    speakers = models.ManyToManyField(Speaker, related_name='speakers')
    abstract = models.TextField(_('abstract'), help_text=_("Maximum 100 words; will be published in the schedule."))
    description = models.TextField(_('description'), help_text=_("Detailed outline for review; will not be published."))
    level = models.CharField(_("audience level"), max_length=20, choices=LEVEL_CHOICES, db_index=True)
    length = models.CharField(_("talk length"), max_length=20, choices=LENGTH_CHOICES, db_index=True)
    review_result = models.IntegerField(_('review result'), editable=False, default=0)

    comments = models.TextField(_('comments'), blank=True, help_text=_('Any other comments or requirements.'))

    accepted = models.BooleanField(_('accepted'))
    scheduled = models.BooleanField(_('scheduled'))

    @property
    def speakers_list(self):
        return ', '.join(['%s' % speaker for speaker in self.speakers.all()])

    def __unicode__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        # Simple denorm so we can easily order Talks based on reveiw outcome
        self.review_result = sum([review.vote for review in self.review_set.all()])
        super(Talk, self).save(*args, **kwargs)

class Review(models.Model):
    VOTE_CHOICES = (
        (-1, 'No'),
        (0,  'Maybe'),
        (1, 'Yes')
    )

    talk = models.ForeignKey(Talk)

    voter = models.ForeignKey(User, verbose_name=_('voter'))
    vote = models.IntegerField(_("vote"), choices=VOTE_CHOICES)
    comments = models.TextField(_('comments'), blank=True, help_text=_('Any other comments or requirements.'))

    class Meta:
        unique_together = (('talk', 'voter'),)

    def __unicode__(self):
        return '%s by %s' % (self.get_vote_display(), self.voter)


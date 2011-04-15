from django.db import models
from django.utils.translation import ugettext_lazy as _


class WaitList(models.Model):
    TICKET_CHOICES = (
        ('corporate', 'Corporate'),
        ('individual', 'Individual'),
        ('student', 'Student'),
    )

    name = models.CharField(_('name'), max_length=75)
    email = models.EmailField(_('e-mail address'))
    organisation = models.CharField(_('organisation / company'), blank=True, max_length=50)

    ticket_type = models.CharField(_("ticket type"), max_length=20, choices=TICKET_CHOICES, db_index=True)
    nr_tickets = models.IntegerField(_("number of tickets"))

    def __unicode__(self):
        return self.name

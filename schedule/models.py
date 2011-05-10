from django.db import models
from talks.models import Talk
from datetime import timedelta, datetime

#class Track(models.Model):
#    name = models.CharField(max_length=75)
#
#    def __unicode__(self):
#        return self.name

class Day(models.Model):
#    track = models.ForeignKey(Track)
    date = models.DateField()

    def __unicode__(self):
        return '%s' % (self.date)

    class Meta:
        ordering = ('date',)

class Slot(models.Model):
    day = models.ForeignKey(Day)
    starttime = models.TimeField()
    length = models.IntegerField(default=45)
    talk = models.ForeignKey(Talk, limit_choices_to={'accepted': True, 'scheduled': False})

    def save(self, *args, **kwargs):
        self.talk.scheduled = True
        self.talk.save()
        super(Slot, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s/%s: %s' % (self.day, self.starttime, self.talk)

    @property
    def endtime(self):
        return self.end_as_datetime.time()

    @property
    def start_as_datetime(self):
        return datetime.combine(self.day.date, self.starttime)

    @property
    def end_as_datetime(self):
        return datetime.combine(self.day.date, self.starttime) + timedelta(minutes=self.length)

    class Meta:
        ordering = ('day__date', 'starttime',)

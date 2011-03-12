from django.db import models
from django.utils.translation import ugettext_lazy as _

class Submission(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    organisation = models.CharField(_('Organisation / Company'), blank=True, max_length=50)
    email = models.EmailField(_('E-mail address'))
    biography = models.TextField(_('Short biography'))
    website = models.CharField(_('Website'), blank=True, max_length=100)
    twitter = models.CharField(_('Twitter'), blank=True, max_length=100)
    linkedin = models.CharField(_('LinkedIn'), blank=True, max_length=100)
    title = models.CharField(_('Title'), max_length=100)
    length = models.IntegerField(_('Length (in minutes)'))
    description = models.TextField(_('Talk description'))
    comments = models.TextField(_('Any other comments / requirements'), blank=True)

    def __unicode__(self):
        return self.title
    

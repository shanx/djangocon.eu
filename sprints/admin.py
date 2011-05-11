from __future__ import absolute_import

from django.contrib import admin
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'organisation', 'attendee', 'thursday', 'friday', 'bed')
    list_filter = ('attendee', 'thursday', 'friday', 'bed',)
    search_fields = ('name', 'email', 'organisation',)


admin.site.register(Participant, ParticipantAdmin)
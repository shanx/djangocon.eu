from __future__ import absolute_import

from django.contrib import admin
from .models import WaitList

class WaitListAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'organisation', 'ticket_type', 'nr_tickets',)
    list_filter = ('ticket_type',)
    search_fields = ('name', 'email', 'organisation',)

admin.site.register(WaitList, WaitListAdmin)
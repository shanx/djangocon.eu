from __future__ import absolute_import

from django.contrib import admin

from .models import Hotel

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'postal_code', 'place',
                    'rate_single', 'rate_double', )

admin.site.register(Hotel, HotelAdmin)

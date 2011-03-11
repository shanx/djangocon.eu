from __future__ import absolute_import

from django.contrib import admin

from .models import Hotel, Reservation

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'postal_code', 'place',
                    'rate_single', 'rate_double', )

admin.site.register(Hotel, HotelAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'title', 'surname', 'initials',
                    'town', 'country', 'phone_number', 'arrival_date',
                     'departure_date', 'nr_of_nights', 'nr_of_guests',
                     'name_second_guest', )

admin.site.register(Reservation, ReservationAdmin)

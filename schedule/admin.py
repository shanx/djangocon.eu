from django.contrib import admin
#from schedule.models import Track, Day, Slot
from schedule.models import Day, Slot

#class TrackAdmin(admin.ModelAdmin):
#    pass
#
#admin.site.register(Track, TrackAdmin)

class DayAdmin(admin.ModelAdmin):
#    list_display = ('date', 'track',)
#    list_filter = ('track',)
    pass

admin.site.register(Day, DayAdmin)

class SlotAdmin(admin.ModelAdmin):
    list_display = ('talk', 'day', 'starttime', 'length',)
    list_filter = ('day',)

admin.site.register(Slot, SlotAdmin)

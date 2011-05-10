from django.contrib import admin

from sorl.thumbnail.admin import AdminImageMixin
from sponsors.models import Sponsor

class SponsorAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'level')
    list_filter = ('level',)

admin.site.register(Sponsor, SponsorAdmin)
from django.contrib import admin
from talks.models import Talk

class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'speakers_list', 'level', 'length', 'accepted', 'scheduled',)
    list_filter = ('level', 'length', 'accepted', 'scheduled',)
    search_fields = ('title', 'abstract',)

admin.site.register(Talk, TalkAdmin)
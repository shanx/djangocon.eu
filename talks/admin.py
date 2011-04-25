from django.contrib import admin
from django.contrib.auth.models import User
from talks.models import Talk, Review

class ReviewInline(admin.TabularInline):
    model = Review
    radio_fields = {'vote': admin.VERTICAL}
    extra = 1
    can_delete = False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "voter":
            kwargs["initial"] = request.user.id
        return super(ReviewInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'speakers_list', 'level', 'length', 'review_result', 'accepted', 'scheduled',)
    list_filter = ('level', 'length', 'accepted', 'scheduled',)
    search_fields = ('title', 'abstract',)
    inlines = (ReviewInline, )
    ordering = ('-review_result',)

    def save_formset(self, request, form, formset, change):
        formset.save()
        # Save form again to have review_result denorm field work
        # This is a quick and ugly hack
        form.save()

admin.site.register(Talk, TalkAdmin)

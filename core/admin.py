from django.contrib import admin
from django.utils.html import format_html

from tasks.models import Task, Plank
from .models import EveryDayReport, EveryWeekReport, PageImage, Page, Review


class EveryWeekReportAdmin(admin.ModelAdmin):
    list_filter = ['user__name', 'date']
    fields = ['user', 'date', 'weight', 'neck', 'waist', 'hips', 'side_view', 'front_view', 'back_view']


class EveryDayReportAdmin(admin.ModelAdmin):
    list_filter = ['user__profile__name', 'date']
    fields = ['date', 'weight', 'steps', 'critical_days', 'file', 'my_clickable_link']

    readonly_fields = ('my_clickable_link',)

    def my_clickable_link(self, instance):
        return format_html(
            '<a href="{0}" target="_blank">{1}</a>',
            instance.link,
            instance.link,
        )

    my_clickable_link.short_description = "Ссылка на отчет"


class PageImageInline(admin.TabularInline):
    model = PageImage
    extra = 1
    classes = ['collapse']


class PageAdmin(admin.ModelAdmin):
    inlines = [PageImageInline,]


admin.site.register(EveryDayReport, EveryDayReportAdmin)
admin.site.register(EveryWeekReport, EveryWeekReportAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Review)
from math import log

from django.contrib import admin
from django.urls import resolve
from django.utils.html import format_html

from core.models import EveryWeekReport
from tasks.models import Task, Plank
from users.models import Profile


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1
    classes = ['collapse']


class PlankInline(admin.TabularInline):
    model = Plank
    extra = 1
    classes = ['collapse']


class EveryWeekReportInline(admin.TabularInline):
    model = EveryWeekReport
    fields = ['date', 'weight', 'neck', 'waist', 'hips', 'fat']
    extra = 1
    classes = ['collapse']
    readonly_fields = ['fat']

    def fat(self, instance):
        return 'fat'

    fat.short_description = '%Жир'


class ProfileAdmin(admin.ModelAdmin):
    inlines = [TaskInline, PlankInline]
    fields = ['name', 'phone', 'growth', 'age', 'gender', 'active', 'my_clickable_link']
    readonly_fields = ('my_clickable_link',)

    def my_clickable_link(self, instance):
        return format_html(
            '<a href="/adminviewresults/{0}/" target="_blank">Посмотреть результаты</a>',
            instance.user.profile.id
        )

    my_clickable_link.short_description = "Результат"


admin.site.register(Profile, ProfileAdmin)

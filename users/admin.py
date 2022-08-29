from django.contrib import admin

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


class ProfileAdmin(admin.ModelAdmin):
    inlines = [TaskInline, PlankInline]


admin.site.register(Profile, ProfileAdmin)

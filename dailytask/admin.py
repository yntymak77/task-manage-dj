from django.contrib import admin

from .models import Task, Step, TaskCompletedTimes


class StepInline(admin.StackedInline):
    model = Step


class TaskCompletedTimesInline(admin.StackedInline):
    model = TaskCompletedTimes


class TaskAdmin(admin.ModelAdmin):
    inlines = [StepInline, TaskCompletedTimesInline, ]


admin.site.register(Task, TaskAdmin)

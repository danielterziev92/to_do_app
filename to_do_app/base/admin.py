from django.contrib import admin

from to_do_app.base.models import Profile
from to_do_app.task.models import Task


class TasksInlineAdmin(admin.StackedInline):
    model = Task
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'day_of_birth')
    inlines = (TasksInlineAdmin, )

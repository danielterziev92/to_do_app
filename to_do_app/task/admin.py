from django.contrib import admin

from to_do_app.task.models import ProjectColor, Priority, Project, Task


@admin.register(ProjectColor)
class ProjectColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority', 'color', 'modify_on')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'due_date', 'is_completed', 'modify_on', 'created_on',)

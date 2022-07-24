from django.db import models

from to_do_app.base.models import AuditEntity


class ProjectColor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Priority(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Project(AuditEntity):
    title = models.CharField(max_length=50)
    priority = models.ForeignKey(to=Priority, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(to=ProjectColor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'projects'
        verbose_name_plural = 'projects'


class Task(AuditEntity):
    title = models.CharField(max_length=150)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tasks'
        verbose_name_plural = 'tasks'

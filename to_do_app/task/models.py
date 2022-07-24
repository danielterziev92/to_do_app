from django.db import models

from to_do_app.base.models import AuditEntity, Profile


class ProjectColor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Project color'


class Priority(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Priority'


class Project(AuditEntity):
    title = models.CharField(max_length=50)
    priority = models.ForeignKey(to=Priority, on_delete=models.CASCADE)
    color = models.ForeignKey(to=ProjectColor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'projects'
        verbose_name_plural = 'Projects'
        ordering = ['priority', ]


class Task(AuditEntity):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tasks'
        verbose_name_plural = 'Tasks'
        ordering = ['due_date', 'id']
        unique_together = ('user_profile', 'title')

from django.urls import path

from to_do_app.task.views import task_edit, task_create, task_delete, project_edit, \
    project_delete, project_create

urlpatterns = (
    path('add/', task_create, name='task create'),
    path('edit/<int:pk>/', task_edit, name='task edit'),
    path('delete/<int:pk>/', task_delete, name='task delete'),

    path('project/add', project_create, name='project create'),
    path('project/edit/<int:pk>/', project_edit, name='project edit'),
    path('project/delete/<int:pk>/', project_delete, name='project delete'),
)

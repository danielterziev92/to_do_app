from django.urls import path

from to_do_app.task.views import tasks_list

urlpatterns = (
    path('', tasks_list, name='task list'),
    path('<int:pk>', task_info, name='task info'),
)

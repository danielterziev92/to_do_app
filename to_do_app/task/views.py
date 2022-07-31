from django.shortcuts import render, redirect

from to_do_app.base.views import get_profile
from to_do_app.task.forms import TaskCreateForm, TaskDeleteForm, TaskEditForm, ProjectCreateForm, ProjectDeleteForm, \
    ProjectEditForm
from to_do_app.task.models import Task, Project


def task_action(request, form_class, instance, success_url, template_file, title):
    if request.method.lower() == 'post':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'title': title,
        'form': form,
        'task': instance,
        'active_additions_nav_items': True,
    }
    return render(request, template_file, context)


def task_create(request):
    return task_action(
        request=request,
        form_class=TaskCreateForm,
        instance=Task(user_profile=get_profile()),
        success_url='dashboard page',
        template_file='create-task.html',
        title='Create task'
    )


def task_edit(request, pk):
    return task_action(
        request=request,
        form_class=TaskEditForm,
        instance=Task.objects.get(pk=pk),
        success_url='dashboard page',
        template_file='update-task.html',
        title='Edit task'
    )


def task_delete(request, pk):
    return task_action(
        request=request,
        form_class=TaskDeleteForm,
        instance=Task.objects.get(pk=pk),
        success_url='dashboard page',
        template_file='delete-task.html',
        title='Delete task'
    )


def project_action(request, form_class, instance, success_url, template_file, title):
    if request.method.lower() == 'post':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)
    context = {
        'title': title,
        'form': form,
        'project': instance,
        'active_additions_nav_items': True,
    }
    return render(request, template_file, context)


def project_create(request):
    return project_action(
        request=request,
        form_class=ProjectCreateForm,
        instance=Project(),
        success_url='dashboard page',
        template_file='create-project.html',
        title='Create project'
    )


def project_edit(request, pk):
    return project_action(
        request=request,
        form_class=ProjectEditForm,
        instance=Project.objects.get(pk=pk),
        success_url='dashboard page',
        template_file='update-project.html',
        title='Edit project'
    )


def project_delete(request, pk):
    return project_action(
        request=request,
        form_class=ProjectDeleteForm,
        instance=Project.objects.get(pk=pk),
        success_url='dashboard page',
        template_file='delete-project.html',
        title='Delete project'
    )

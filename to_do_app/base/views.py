from django.shortcuts import render

from to_do_app.base.models import Profile
from to_do_app.task.models import Project, Task


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_tasks():
    task_list = True


def home_page(request):
    context = {
        'title': "Home Page"
    }

    return render(request, 'index.html', context)


def dashboard_page(request):
    profile = get_profile()
    profile_full_name = f'{profile.first_name} {profile.last_name}'
    task_count = profile.task_set.count()
    projects = Project.objects.all()
    # tasks_list = profile.task_set.filter(project__task__user_profile_id=profile)
    # tasks_list = profile.task_set.all().filter(project__task__title__in=projects)
    # tasks_list = profile.task_set.filter(project__title__in=projects)
    tasks_list = Task.objects.filter(project__in=projects)
    # task_count = tasks_list.count()
    context = {
        'title': 'Dashboard',
        'active_additions_nav_items': True,
        'profile_full_name': profile_full_name,
        'tasks_list': tasks_list,
        'task_count': task_count,
        'projects': projects,
    }

    return render(request, 'dashboard.html', context)


def profile_page(request):
    context = {
        'title': 'Profile'
    }

    return render(request, 'profile.html', context)

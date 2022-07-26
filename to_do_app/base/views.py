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
    projects_set = Task.objects.prefetch_related('project__task_set').values_list('project__title', 'id', 'title',
                                                                                  'is_completed',
                                                                                  'due_date').order_by('project_id')

    projects_list = dict()
    for project, id, title, is_completed, due_date in projects_set:
        info = id, title, is_completed, due_date
        projects_list.setdefault(project, []).append(info)

    context = {
        'title': 'Dashboard',
        'active_additions_nav_items': True,
        'profile_full_name': profile_full_name,
        'projects_list': projects_list,
    }

    return render(request, 'dashboard.html', context)


def profile_page(request):
    context = {
        'title': 'Profile'
    }

    return render(request, 'profile.html', context)

from django.shortcuts import render, redirect

from to_do_app.base.forms import ProfileCreteForm, ProfileEditForm, ProfileDeleteForm
from to_do_app.base.models import Profile
from to_do_app.task.models import Task


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    context = {
        'title': "Home Page"
    }

    return render(request, 'index.html', context)


def dashboard_page(request):
    profile = get_profile()
    profile_full_name = f'{profile.first_name} {profile.last_name}'
    projects_set = Task.objects.filter(user_profile=profile) \
        .prefetch_related('project__task_set') \
        .values_list('project__title', 'project_id', 'id', 'title', 'is_completed', 'due_date') \
        .order_by('project_id', 'due_date')

    projects_list = dict()
    for project, project_id, id, title, is_completed, due_date in projects_set:
        info = project_id, id, title, is_completed, due_date
        projects_list.setdefault(project, []).append(info)

    context = {
        'title': 'Dashboard',
        'active_additions_nav_items': True,
        'profile_full_name': profile_full_name,
        'projects_list': projects_list,
    }

    return render(request, 'dashboard.html', context)


def profile_page(request):
    profile = get_profile()
    total_task = profile.task_set.filter(user_profile=profile).count()
    context = {
        'title': 'Profile',
        'profile': get_profile(),
        'total_tasks': total_task,
        'profile_id': get_profile().pk,
    }

    return render(request, 'profile.html', context)


def profile_action(request, form_class, instance, success_url, template_file, title):
    if request.method.lower() == 'post':
        profile_form = form_class(request.POST, request.FILES, instance=instance)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(success_url)
    else:
        profile_form = form_class(instance=instance)
    context = {
        'title': title,
        'form': profile_form
    }
    return render(request, template_file, context)


def profile_create(request):
    return profile_action(
        request=request,
        form_class=ProfileCreteForm,
        instance=Profile(),
        success_url='home page',
        template_file='create_profile.html',
        title='Create profile'
    )


def profile_edit(request):
    return profile_action(
        request=request,
        form_class=ProfileEditForm,
        instance=get_profile(),
        success_url='profile page',
        template_file='update_profile.html',
        title='Edit profile'
    )


def profile_delete(request):
    return profile_action(
        request=request,
        form_class=ProfileDeleteForm,
        instance=get_profile(),
        success_url='home page',
        template_file='delete_profile.html',
        title='Delete profile'
    )

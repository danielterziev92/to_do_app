from django.shortcuts import render


def tasks_list(request):

    context = {
        'title': 'Tasks List'
    }

    return render(request, '', context)



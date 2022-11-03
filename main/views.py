from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from main.models import Task


# REMEMBER THAT LOGINREQUIRED DECORATOR NLY FOR FUNCTIONS . FOR CLASS BASED USE MIXIN!
@login_required
def main_view(request):
    user = request.user

    tasks = Task.objects.filter(user=user)
    context = {'user': user, 'tasks': tasks}
    return render(request, 'main/index.html', context)


@login_required
def addTask(request):
    user = request.user
    name = request.POST.get('taskname')
    Task.objects.create(name=name, user=user)
    # ret a template with all tasks
    tasks = user.tasks.all()
    return render(request, 'main/partials/task_list.html', {'tasks': tasks})


@login_required
@require_http_methods(['DELETE'])
def delTask(request, pk):
    Task.objects.get(id=pk).delete()
    tasks = request.user.tasks.all()
    return render(request, 'main/partials/task_list.html', {'tasks': tasks})

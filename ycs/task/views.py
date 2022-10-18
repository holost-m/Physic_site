from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Topic, Task


def create(request):
    topics = Topic.objects.all()
    if request.method == "POST":
        new_task = Task()
        new_task.topic = Topic.objects.get(topic=request.POST.get("topic"))
        new_task.name = request.POST.get("name")
        new_task.text = request.POST.get("text")
        new_task.file = request.POST.get("file")
        vars = request.POST.get("variables")
        vars = {k: v for k, v in (line.split(' = ') for line in vars.split('\n'))}
        print(vars)
        # new_task.variables_and_si =
        new_task.save()
        return render(request, 'task/base.html', {"topics": topics})
    else:

        return render(request, 'task/base.html', {"topics": topics})

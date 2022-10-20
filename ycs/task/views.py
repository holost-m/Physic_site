from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Topic, Task
from .my_functions import give_variables_and_si, give_correct_solving


def create(request):
    topics = Topic.objects.all()
    if request.method == "POST":
        new_task = Task()
        new_task.topic = Topic.objects.get(topic=request.POST.get("topic"))
        new_task.name = request.POST.get("name")
        new_task.text = request.POST.get("text")
        new_task.file = request.POST.get("file")
        vars = request.POST.get("variables")
        si = request.POST.get("si_system")
        new_task.variables_and_si = give_variables_and_si(vars, si)
        new_task.to_find = request.POST.get("to_find")
        new_task.solving = give_correct_solving(request.POST.get("solving"))
        new_task.answer = request.POST.get("answer")
        print(new_task.__dict__)
        new_task.save()
    return render(request, 'task/base.html', {"topics": topics})

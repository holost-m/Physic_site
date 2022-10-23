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
    return render(request, 'task/create.html', {"topics": topics})

def delete(request):
    if request.method == "POST": # Удаляем запись по запросу
        delete_task = Task.objects.get(id=request.POST.get("task_id_delete"))
        delete_task.delete()
    task_list = list(Task.objects.all().values('topic', 'name', 'text', 'id').order_by('topic'))
    for dct in task_list:
        dct['topic_name'] = Topic.objects.get(id=dct['topic'])

    return render(request, 'task/delete.html', {"task_list": task_list})

def change(request):
    task_list = list(Task.objects.all().values('topic', 'name', 'id').order_by('topic'))
    for dct in task_list:
        dct['topic_name'] = Topic.objects.get(id=dct['topic'])
    return render(request, 'task/change.html', {"task_list": task_list})

def solve(request):

    return render(request, 'task/solve.html')

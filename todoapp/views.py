from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Todo


def todoView(request):
    todo = Todo.objects.all()
    return render(request, "todoView.html", {"todo": todo})


def addTodo(request):
    new_item = Todo(quest = request.POST["quest"])
    new_item.save()
    return HttpResponseRedirect("/todo/")


def deleteTodo(request, todo_id):
    delete_item = Todo.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect("/todo/")


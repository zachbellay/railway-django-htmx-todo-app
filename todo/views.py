from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Todo


def todo(request):
    context = {
        "todos": Todo.objects.all(),
    }
    return render(request, "todo.html", context)


def add_todo(request):
    if request.htmx:
        todo = Todo.objects.create(
            description=request.POST.get("todo"),
            completed=False,
        )

        return HttpResponse(
            f"<li id='todo-{todo.id}'><input type='checkbox' name='todo-{todo.id}'><span>{todo.description}</span></li>"
        )

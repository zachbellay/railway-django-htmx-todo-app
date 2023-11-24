from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Todo


def todo(request):
    context = {"todos": Todo.objects.all()}
    return render(request, "todo.html", context)


def add_todo(request):
    if request.htmx:
        todo = Todo.objects.create(
            description=request.POST.get("todo"),
            completed=False,
        )

        return render(request, "partials/todo.html", {"todo": todo})


def delete_todo(request, pk):
    if request.htmx:
        Todo.objects.get(pk=pk).delete()
        return HttpResponse("")

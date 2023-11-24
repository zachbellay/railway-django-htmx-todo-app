from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from todo.models import Todo


@require_GET
def todo(request):
    context = {"todos": Todo.objects.all()}
    return render(request, "todo.html", context)


@require_POST
def add_todo(request):
    if request.htmx:
        todo = Todo.objects.create(
            description=request.POST.get("todo"),
            completed=False,
        )

        return render(request, "partials/todo.html", {"todo": todo})


@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    if request.htmx:
        Todo.objects.get(pk=pk).delete()
        return HttpResponse("")

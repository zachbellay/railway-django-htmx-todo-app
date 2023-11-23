from django.http import HttpResponse


def add_todo(request):
    return HttpResponse("added todo")

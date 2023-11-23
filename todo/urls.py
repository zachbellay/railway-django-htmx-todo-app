from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="todo.html"), name="home"),
]


htmxpatterns = [
    path("htmx/add-todo/", views.add_todo, name="add-todo"),
]

urlpatterns += htmxpatterns

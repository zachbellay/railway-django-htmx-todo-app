from django.urls import path

from . import views

urlpatterns = [
    path("", views.todo, name="todo"),
]


htmxpatterns = [
    path("htmx/add-todo/", views.add_todo, name="add-todo"),
    path("htmx/delete-todo/<int:pk>/", views.delete_todo, name="delete-todo"),
]

urlpatterns += htmxpatterns

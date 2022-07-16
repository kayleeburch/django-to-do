from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("all_todos/", views.all_todos),
    path("signup/", views.signup),
    path("login/", views.log_in),
    path("logout/", views.log_out),
    path("new/", views.add_item),
    path("<int:todo_id>/", views.get_details),
    path("<int:todo_id>/edit/", views.update_item),
    path("<int:todo_id>/delete/", views.delete_view),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("signup/", views.signup),
    path("new/", views.add_item),
    path("<int:todo_id>/", views.get_details),
    path("<int:todo_id>/edit/", views.update_item),
    path("<int:todo_id>/delete/", views.delete_view),
]
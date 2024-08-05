from django.urls import path
from . import views

urlpatterns = [
    path("create-userprofile/", views.create_userprofile, name="create-userprofile"),
    path("view-userprofile/", views.view_userprofile, name="view-userprofile"),
]

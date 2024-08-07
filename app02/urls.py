from django.urls import path
from . import views

urlpatterns = [
    path("create-userprofile/", views.create_userprofile, name="create-userprofile"),
    path("userprofile-view/", views.userprofile_view, name="userprofile-view"),
    path("edit-userprofile/", views.edit_userprofile, name="edit-userprofile"),
]

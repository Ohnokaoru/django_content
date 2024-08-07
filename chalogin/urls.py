from django.urls import path, include
from . import views

urlpatterns = [
    path("user-chalogin/", views.user_chalogin, name="user-chalogin"),
]

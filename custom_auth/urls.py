from django.urls import path
from .views import LoginAPI, ResgisterAPI

urlpatterns = [
    path("login/", LoginAPI.as_view()),
    path("register/", ResgisterAPI.as_view()),
]

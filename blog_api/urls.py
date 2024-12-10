from django.urls import path
from .views import PostCreate, PostRetriveByID, PostSearch, UserProfile

urlpatterns = [
    path("post/", PostCreate.as_view()),
    path("post/<int:pk>/", PostRetriveByID.as_view()),
    path("search/", PostSearch.as_view()),
    path("profile/", UserProfile.as_view()),
]

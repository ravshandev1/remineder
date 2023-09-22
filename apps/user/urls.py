from django.urls import path
from .views import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
    path('', UserAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view()),
]

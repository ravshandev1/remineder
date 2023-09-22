from django.urls import path
from .views import PostAPI, PostRetrieveAPI, PostsAPI, CommentAPI

urlpatterns = [
    path('', PostAPI.as_view()),
    path('<int:pk>/', PostRetrieveAPI.as_view()),
    path('posts/', PostsAPI.as_view()),
    path('comment/<int:pk>/', CommentAPI.as_view()),
]

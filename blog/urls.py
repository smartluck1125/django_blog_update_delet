from django.urls import path
from .views import (
  PostListView,
  PostCreateView,
  UserPostListView,
  PostDetailView,
)
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail' )
]

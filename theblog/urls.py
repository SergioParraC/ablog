from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('list', HomeView.as_view(), name='list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='articleDetail'),
    path('addpost', AddPostView.as_view(), name='create_post'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name='updatePost'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='deletePost'),
]

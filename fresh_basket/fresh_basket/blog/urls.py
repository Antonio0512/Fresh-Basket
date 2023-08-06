from django.urls import path
from . import views

urlpatterns = [
    path('posts-all/', views.PostsListView.as_view(), name='posts-all'),
    path('<int:pk>/post-details/', views.PostDetailsView.as_view(), name='post-details'),
    path('post-add/', views.PostAddPageView.as_view(), name='post-add-page'),
    path('create/', views.CreatePostView.as_view(), name='post-add')
]

from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('post/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-retrieve-update-destroy')
]
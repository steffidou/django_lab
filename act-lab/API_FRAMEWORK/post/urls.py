from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('post/', PostListCreateAPIView.as_view(), name = 'list-create-post'),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name = 'retrieve-update-destroy-post')
]
"""REST API URL configuration (versioned under ``/api/v1/``)."""

from django.urls import path

from authentication.api_views import UserListCreateAPIView, UserDetailAPIView
from author.api_views import AuthorListCreateAPIView, AuthorDetailAPIView

urlpatterns = [
    # Users
    path("user/", UserListCreateAPIView.as_view(), name="api_user_list"),
    path("user/<int:pk>/", UserDetailAPIView.as_view(), name="api_user_detail"),
    # Authors
    path("author/", AuthorListCreateAPIView.as_view(), name="api_author_list"),
    path("author/<int:pk>/", AuthorDetailAPIView.as_view(), name="api_author_detail"),
]

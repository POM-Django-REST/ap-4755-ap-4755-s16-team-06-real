from rest_framework import generics

from .models import CustomUser
from .serializers import UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    """``GET /api/v1/user/`` list users, ``POST`` create a user."""

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """``GET/PUT/PATCH/DELETE /api/v1/user/{id}`` for a single user."""

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

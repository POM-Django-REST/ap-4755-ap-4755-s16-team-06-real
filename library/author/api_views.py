from rest_framework import generics

from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    """``GET /api/v1/author/`` list authors, ``POST`` create an author."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """``GET/PUT/PATCH/DELETE /api/v1/author/{id}`` for a single author."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

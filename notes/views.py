from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from notes.models import Note
from notes.serializers import NoteSerializer, CategorySerializer
from notes.filters import NoteFilter

class NoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = NoteFilter

class NoteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'id'

class CategoryListAPIView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = CategorySerializer

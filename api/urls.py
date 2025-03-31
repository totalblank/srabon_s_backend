from django.urls import path, include
from notes.views import NoteListCreateAPIView, NoteRetrieveUpdateDestroyAPIView, CategoryListAPIView

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view()),
    path('notes/<int:id>', NoteRetrieveUpdateDestroyAPIView.as_view()),
    path('notes/categories', CategoryListAPIView.as_view()),
]

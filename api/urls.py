from django.urls import path, include
from notes.views import (
        NoteListCreateAPIView,
        NoteRetrieveUpdateDestroyAPIView,
        CategoryListAPIView
)

from flashcard.views import (
    FlashCardListCreateAPIView,
    FlashCardRetrieveUpdateDestroyAPIView,
    FlashCardCategoryListAPIView
)

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view()),
    path('notes/<int:id>', NoteRetrieveUpdateDestroyAPIView.as_view()),
    path('notes/categories', CategoryListAPIView.as_view()),

    path('flashcards/', FlashCardListCreateAPIView.as_view()),
    path('flashcards/<int:id>', FlashCardRetrieveUpdateDestroyAPIView.as_view()),
    path('flashcards/categories', FlashCardCategoryListAPIView.as_view()),
]

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from flashcard.models import FlashCard
from flashcard.serializers import FlashCardSerializer, FlashCardCategorySerializer
from flashcard.filters import FlashCardFilter

class FlashCardListCreateAPIView(generics.ListCreateAPIView):
    queryset = FlashCard.objects.all().order_by('front')
    serializer_class = FlashCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = FlashCardFilter

class FlashCardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'id'

class FlashCardCategoryListAPIView(generics.ListAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardCategorySerializer

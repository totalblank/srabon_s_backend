import django_filters

from flashcard.models import FlashCard

class FlashCardFilter(django_filters.FilterSet):
    class Meta:
        model = FlashCard
        fields = {
            'category': ['icontains'],
            'front': ['icontains'],
            'back': ['icontains'],
            'author': ['iexact'],
        }

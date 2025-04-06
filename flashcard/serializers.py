from rest_framework import serializers
from django.contrib.auth.models import User

from flashcard.models import FlashCard

class FlashCardSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField()

    class Meta:
        model = FlashCard
        fields = (
            'id',
            'author',
            'author_name',
            'front',
            'back',
            'category',
        )

class FlashCardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ('category',)

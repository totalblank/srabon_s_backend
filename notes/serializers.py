from rest_framework import serializers
from django.contrib.auth.models import User

from notes.models import Note

class NoteSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField()

    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'author',
            'author_name',
            'date_created',
            'content',
            'category',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('category',)

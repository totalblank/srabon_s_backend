import django_filters

from notes.models import Note

class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = {
            'title': ['icontains'],
            'category': ['icontains'],
        }

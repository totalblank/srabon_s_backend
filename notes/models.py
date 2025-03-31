from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    date_created = models.DateField(auto_created=True)
    content = models.TextField() # markdown text
    
    # cateogory:subcategory
    category = models.CharField(max_length=256)

    # TODO: Add Images
    
    @property
    def author_name(self):
        return self.author.username


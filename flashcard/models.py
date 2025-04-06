from django.db import models
from django.contrib.auth.models import User

class FlashCard(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()
    category = models.CharField(max_length=256)

    @property
    def author_name(self):
        return self.author.username

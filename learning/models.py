from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):

    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fastfood'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    lattitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating: {self.rating}"

class Sale(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sales'
    )
    income = models.DecimalField(
        decimal_places=2,
        max_digits=8
    )
    datetime = models.DateTimeField()

    def __str__(self):
        return f"\nFor restaurant: {self.restaurant.name}\nIncome: {self.income}\nat: {self.datetime}\n"

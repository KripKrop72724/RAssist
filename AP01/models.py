from django.db import models
from django.contrib.auth.models import User


# Restaurant model
# User model
# Rating model
# Sales model

class Restaurant(models.Model):
    class RestaurantTypes(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ARABIC = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=RestaurantTypes.choices)

    def __str__(self):
        print("Name of the hotel is " + self.name)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        print("Rating: " + str(self.rating))


class RatingImages(models.Model):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='rating_images/')

    def __str__(self):
        return f"Image for rating {self.rating.id}"


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
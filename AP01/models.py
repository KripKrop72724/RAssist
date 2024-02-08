from django.db import models
from django.contrib.auth.models import User


# Restaurant model
# User model
# Rating model


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

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

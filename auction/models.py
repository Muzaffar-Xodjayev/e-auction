from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="listing", default="img/default_model.png")
    description = models.TextField()
    price = models.IntegerField(default=0)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    listing_id = models.ForeignKey(Listing, models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.author


class Bid(models.Model):
    listing_id = models.ForeignKey(Listing, models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.IntegerField(default=0)

    def __str__(self):
        return self.author


class WatchList(models.Model):
    listing_id = models.ForeignKey(Listing, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.listing_id

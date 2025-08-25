from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Listing(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="listings/", default="/default/default_model.png")
    description = models.TextField()
    price = models.IntegerField(default=0)
    is_publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    listing_id = models.ForeignKey(Listing, models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    test = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.author)


class Bid(models.Model):
    listing_id = models.ForeignKey(Listing, models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.IntegerField(default=0)

    def __str__(self):
        return str(self.author)


class WatchList(models.Model):
    listing_id = models.ForeignKey(Listing, models.CASCADE, primary_key=True)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return str(self.listing_id)

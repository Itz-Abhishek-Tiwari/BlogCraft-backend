from django.db import models
# from django.contrib.auth.models import User


class Category(models.Model):
    ELECTRONICS = "electronics"
    FASHION = "fashion"
    HOME = "home"
    SPORTS = "sports"
    TOYS = "toys"

    Category_choice = [
        (ELECTRONICS, "Electronics"),
        (FASHION, "Fashion"),
        (HOME, "Home"),
        (SPORTS, "Sports"),
        (TOYS, "Toys"),
    ]

    name = models.CharField(max_length=20, choices=Category_choice, default=ELECTRONICS)

    def __str__(self):
        return self.get_name_display()


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    categorys = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

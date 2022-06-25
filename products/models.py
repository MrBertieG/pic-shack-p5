from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        """Products in descending order"""
    
        ordering = ["-created_on"]

    
    def __str__(self):
        return self.name


RATE_CHOICES = [
    (1, "1 - Will not recommend"),
    (2, "1 - Could be beter"),
    (3, "1 - It's ok"),
    (4, "1 - I love it!"),
]


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reviews"
    )
    product = models.ForeignKey(
        Product, related_name="product_reviews", on_delete=models.CASCADE
    )
    text = models.TextField(max_length=250)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        """Reviews in descending order"""

        ordering = ["-created_on"]

    def __str__(self):
        return str(self.id)

from django.db import models
from .Category import Category

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField(null=False)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title

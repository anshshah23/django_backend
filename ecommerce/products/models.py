from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    short_desc = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

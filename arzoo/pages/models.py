from django.db import models



class Cart(models.Model):
    name = models.CharField(max_length=100)  # Example field for product name
    price = models.IntegerField()  # Example field for product price

    def __str__(self):
        return self.name

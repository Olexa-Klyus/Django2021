from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    # використання валідаторів
    # brand = models.CharField(max_length=100)
    # price = models.IntegerField(validators=(MaxValueValidator(100000), MinValueValidator(100)))
    # year = models.IntegerField()
    # create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now=True)

    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

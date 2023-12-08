from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.auto_parks.models import AutoParksModel

from .managers import CarManager


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
    auto_park = models.ForeignKey(AutoParksModel, on_delete=models.CASCADE, related_name='cars')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = CarManager()

    def __str__(self):
        return self.brand

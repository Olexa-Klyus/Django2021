from django.contrib.auth import get_user_model
from django.db import models

from apps.auto_salons.models import AutoSalonsModel

UserModel = get_user_model()


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    year = models.IntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
    auto_salon = models.ForeignKey(AutoSalonsModel, on_delete=models.CASCADE, related_name='cars', blank=True,
                                   null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

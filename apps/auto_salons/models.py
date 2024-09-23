from django.contrib.auth import get_user_model
from django.db import models

from apps.users.models import ProfileModel

UserModel = get_user_model()


class AutoSalonsModel(models.Model):
    class Meta:
        db_table = 'auto_salons'

    name = models.CharField(max_length=20)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,
                                related_name='autosalon', blank=True, null=True)

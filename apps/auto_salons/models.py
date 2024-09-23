from django.db import models

from apps.users.models import ProfileModel


class AutoSalonsModel(models.Model):
    class Meta:
        db_table = 'auto_salons'

    name = models.CharField(max_length=20)
    user_profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='auto_salon', blank=True,
                                        null=True)

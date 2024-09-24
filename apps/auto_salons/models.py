from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class AutoSalonsModel(models.Model):
    class Meta:
        db_table = 'auto_salons'

    name = models.CharField(max_length=20)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_salons')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
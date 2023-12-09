from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from .enums import RegEx
from .managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'
        ordering = ['id']

    email = models.EmailField(unique=True)
    # валідуємо пароль
    password = models.CharField(max_length=255, validators=[
        RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.msg)
    ])
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # якщо потрібно робити логінацію через email а не як стандартно через username, змінюємо поле USERNAME_FIELD
    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    surname = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.msg)])
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(150)])
    phone = models.CharField(max_length=10, validators=[RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.msg)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')

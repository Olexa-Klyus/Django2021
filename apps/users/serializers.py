from typing import Type

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from .models import ProfileModel, UserModel

# щоб дістатися иетодів, які ми створювали в UserModel, потрібно типізувати UserModel (використовуємо Type)
UserModel: Type[UserModel] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'create_at', 'updated_at',
            'profile'
        )
        read_only_fields = (
            'id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'create_at', 'updated_at', 'profile')

        # щоб не показувався хешований пароль, потрібно в extra_kwarks словник передати значення
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic  # створюємо контроль транзакцій, щоб відкотити створення usera якщо не створиться профіль
    def create(self, validated_data: dict):
        # щоб записати в базу, видаляємо з валідованого юзера профіль
        profile = validated_data.pop('profile')

        # використовуємо наш створений метод
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user

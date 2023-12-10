import os
from typing import Type

from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.db import transaction
from django.template.loader import get_template

from rest_framework.serializers import ModelSerializer, ValidationError

from .models import ProfileModel, UserModel

# щоб дістатися методів, які ми створювали в UserModel, потрібно типізувати UserModel (використовуємо Type)
UserModel: Type[UserModel] = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        exclude = ('user',)


class AddAvatarSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)


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

    # можна зробити додаткову валідацію через метод validate
    # додаткова валідація спрацьовує тільки після основної, яку проводять серіалайзери і яка закладена в моделі,
    # якщо там все ок - тоді в методі validate можна зробити додаткову валідацію
    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']
        if email == password:
            raise ValidationError({'email_eq_password': 'email equal password'})
        # return super().validate(attrs)
        # можна просто attrs повертати
        return attrs

    # Ще один варіант додаткової валідації - через додавання до validate через нижнє підкреслення назви поля,
    # по якому потрібна валідація - тут значення поля profile попадає у value
    def validate_profile(self, value):
        name: str = value['name']
        if name.lower() == 'max':
            raise ValidationError('name equal Max')
        return value

    @transaction.atomic  # створюємо контроль транзакцій, щоб відкотити створення usera якщо не створиться профіль
    def create(self, validated_data: dict):
        # щоб записати в базу, видаляємо з валідованого юзера профіль
        profile = validated_data.pop('profile')

        # використовуємо наш створений метод
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)

        template = get_template('register.html')
        html_content = template.render()
        msg = EmailMultiAlternatives('Register', from_email=os.environ.get('EMAIL_HOST_USER'), to=[user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return user

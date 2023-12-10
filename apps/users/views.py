from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from .serializers import AddAvatarSerializer, UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    # якщо прописати в класі наступне, на виході буде json обєкт, але щоб в кожному класі не прописувати
    # прописуємо раз у extra_kwargs і звязуємо з settings
    # renderer_classes = (JSONRenderer,)

    permission_classes = (AllowAny,)


class AddAvatarView(UpdateAPIView):
    # дозволяємо тільки patch метод
    http_method_names = ('patch',)

    serializer_class = AddAvatarSerializer

    def get_object(self):
        return self.request.user.profile

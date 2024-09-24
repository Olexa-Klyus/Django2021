from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny

from .models import AutoSalonsModel
from .serializers import AutoSalonSerializer


class AutoSalonsListCreateView(ListCreateAPIView):
    queryset = AutoSalonsModel.objects.all()
    serializer_class = AutoSalonSerializer

    def get_queryset(self):
        print('user - ', self.request.user, self.request.user.id)
        qs = self.queryset.all().filter(user=self.request.user)

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoSalonsListView(ListAPIView):
    queryset = AutoSalonsModel.objects.all()
    serializer_class = AutoSalonSerializer

    permission_classes = (AllowAny,)

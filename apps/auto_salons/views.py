from rest_framework.generics import ListCreateAPIView

from .models import AutoSalonsModel
from .serializers import AutoSalonSerializer


class AutoSalonListCreateView(ListCreateAPIView):
    queryset = AutoSalonsModel.objects.all()
    serializer_class = AutoSalonSerializer

    # def get_queryset(self):
    #     print('user - ', self.request.user.profile.name, self.request.user.autosalon.name)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

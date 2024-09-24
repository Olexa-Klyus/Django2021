from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        print('user - ', self.request.user, self.request.user.id)
        qs = self.queryset.all()
        price_gt = self.request.query_params.get('price_gt')
        auto_park_id = self.request.query_params.get('auto_park_id')

        if price_gt:
            qs = qs.filter(price__gt=price_gt)
        if auto_park_id:
            qs = qs.filter(auto_park_id=auto_park_id)

        return qs



class CarUpdateRetriveDestroy(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def perform_update(self, serializer):
        print(self.request.user.id)
        print(serializer)
        qs = self.queryset.all()
        print(qs)

        serializer.save()

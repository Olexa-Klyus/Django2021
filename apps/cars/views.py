from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import CarModel
from .serializers import CarSerializer


# витягнути кари по id автопарку
class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllowAny,)

    # authentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)

    # # щоб зробити фільтр переопреділяємо get_queryset,
    # # якщо параметр є в запиті, фільтруємо по ньому, якщо ні повертаємо без змін
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
    permission_classes = (AllowAny,)

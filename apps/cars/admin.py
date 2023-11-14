from django.contrib import admin
from .models import CarModel


# найпростіший спосіб привязати таблицю в адмінку
# admin.site.register(CarModel)

# або створити клас
@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'price')

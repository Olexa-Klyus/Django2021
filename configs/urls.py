import django.conf.urls.static as static
# from django.contrib import admin
from django.urls import include, path

from configs import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth', include('apps.auth.urls')),
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('users', include('apps.users.urls'))
]
# для роботи і зберігання фотографій додаємо
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

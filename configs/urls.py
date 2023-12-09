from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import include, path

from configs import settings

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('users', include('apps.users.urls'))
]
# для роботи і зберігання фотографій додаємо
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

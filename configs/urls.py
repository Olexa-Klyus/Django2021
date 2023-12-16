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
# для відхоплення 400 і 500 помилок і повідомлення в json форматі є наступне:
# але працює тільки при DEBUG = False
handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'

# для роботи і зберігання фотографій додаємо
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

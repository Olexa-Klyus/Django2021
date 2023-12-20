from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view

from rest_framework.permissions import AllowAny

# from django.contrib import admin


schema_view = get_schema_view(
    openapi.Info(
        title="Autoparks API",
        default_version='v1',
        description="About cars",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('cars', include('apps.cars.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('users', include('apps.users.urls')),
    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-redoc'),
]
# для відхоплення 400 і 500 помилок і повідомлення в json форматі є наступне:
# але працює тільки при DEBUG = False
handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'

# для роботи і зберігання фотографій додаємо
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

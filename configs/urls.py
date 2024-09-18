# from django.contrib import admin
from django.urls import path, include

from first.views import FirstView
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('first', FirstView.as_view())

]

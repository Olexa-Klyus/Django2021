# from django.contrib import admin
from django.urls import path, include

from first.views import FirstView, SecondView, ThirdView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('first', FirstView.as_view()),
    path('second', SecondView.as_view()),
    path('third/<str:name>/<int:age>', ThirdView.as_view()),

]

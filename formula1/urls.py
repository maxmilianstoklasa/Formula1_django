# Import modulu path z balíku django.urls
from django.urls import path
# Import modulu views (soubor views.py) ze stejné složky (.)
from . import views

# URL mapování - seznam URL adres pro aplikaci movies
urlpatterns = [
    path('', views.index, name='index'),
    path('racer/', views.DriverList.as_view(), name="driver_list"),
    path('racer/<int:pk>/', views.DriverDetail.as_view(), name="driver_detail"),
    path('constructors/<str:constructor_name>/', views.DriverList.as_view(), name='driver_team'),
]

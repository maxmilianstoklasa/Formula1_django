# Import modulu path z balíku django.urls
from django.urls import path
# Import modulu views (soubor views.py) ze stejné složky (.)
from . import views

# URL mapování - seznam URL adres pro aplikaci movies
urlpatterns = [
    path('', views.index, name='index'),
    path('racer/', views.DriverList.as_view(), name="driver_list"),
    path('racer/<int:pk>/', views.DriverDetail.as_view(), name="driver-detail"),
    path('constructors/<str:constructor_name>/', views.DriverList.as_view(), name='driver_team'),
    path('racers/create', views.DriverCreateView.as_view(), name="driver_create"),
    path('racers/<int:pk>/update', views.DriverUpdateView.as_view(), name="driver_update"),
    path('racers/<int:pk>/delete', views.DriverDeleteView.as_view(), name="driver_delete"),
]

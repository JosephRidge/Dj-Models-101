from django.urls import path
from .views import home 

urlpatterns = [
    path('', views.home, name='home'), 

    path('create-ocean', views.createOcean, name="create-ocean"),
    path('read-oceans', views.readOceans, name="read-oceans"),
    path('read-ocean/<str:pk>', views.readOcean, name="read-ocean"),
    path('update-ocean/<str:pk>', views.updateOcean, name="update-ocean"),
    path('delete-lake/<str:pk>', views.deleteOcean, name="delete-ocean"),

    path('create-lake', views.createLake, name="create-lake"),
    path('read-lakes', views.readLakes, name="read-lakes"),
    path('read-lake/<str:pk>', views.readLake, name="read-lake"),
    path('update-lake/<str:pk>', views.updateLake, name="update-lake"),
    path('delete-lake/<str:pk>', views.deleteLake, name="delete-lake")
]
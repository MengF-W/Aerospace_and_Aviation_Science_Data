from django.urls import path
from . import views, services_api

urlpatterns = [
    path('', views.apod, name='apod'),
    path('api/v1/apod_api', services_api.apod_api, name='apod_api')
]
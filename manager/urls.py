from django.urls import path
from .views import Planer

urlpatterns = [
    path('', Planer.as_view(), name='Planers-title')
]
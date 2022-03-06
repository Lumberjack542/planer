from django.urls import path
from .views import Planer, create

urlpatterns = [
    path('', Planer.as_view(), name='Planers-title'),
    path('create', create, name='Planer-form')
]
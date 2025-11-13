from django.urls import path
from . import views

urlpatterns = [
    path('detect/', views.detect_damage_api, name='detect_damage'),
]

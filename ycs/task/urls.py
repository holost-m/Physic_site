from django.urls import path, re_path
from .views import create

# Список адресов для приложения exercise_physic

urlpatterns = [
    path('create', create),
]
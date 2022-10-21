from django.urls import path, re_path
from .views import create, delete, change, solve

# Список адресов для приложения exercise_physic

urlpatterns = [
    path('create', create),
    path('delete', delete),
    path('change', change),
    path('solve', solve),
]
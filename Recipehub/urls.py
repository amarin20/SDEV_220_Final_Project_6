from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_path, name='recipe_path'),
]
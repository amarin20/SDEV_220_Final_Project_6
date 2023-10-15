from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_path, name='recipe_path'),
    path('upload_recipe/', views.upload_recipe_view, name='upload_recipe'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/new/', views.recipe_create, name='recipe_create'),
    path('recipes/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
]
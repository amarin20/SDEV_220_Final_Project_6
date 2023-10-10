from django.contrib import admin
from .models import Category, Recipe, Ingredient, equipment, RecipeIngredient, RecipeEquipment
# Register your models here.

admin.site.register (Category)
admin.site.register (Recipe)
admin.site.register (Ingredient)
admin.site.register (equipment)
admin.site.register (RecipeIngredient)
admin.site.register (RecipeEquipment)
from django.shortcuts import render
from django.utils import timezone
from .models import Recipe, RecipeIngredient, RecipeEquipment
from django.shortcuts import render, get_object_or_404


def recipe_list(request):
    recipe_post = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    for recipe in recipe_post:
        recipe.formatted_profit = recipe.profit_calculator()
        recipe.recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        recipe.recipe_equipment = RecipeEquipment.objects.filter(recipe=recipe)
    return render(request, 'Recipehub/recipe_list.html', {'recipe_post': recipe_post})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.formatted_profit = recipe.profit_calculator()
    recipe.recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    recipe.recipe_equipment = RecipeEquipment.objects.filter(recipe=recipe)
    return render(request, 'Recipehub/recipe_detail.html', {'recipe': recipe})
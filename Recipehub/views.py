import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Ingredient, Recipe, RecipeIngredient
from .forms import UploadRecipeForm, RecipeForm 

def recipe_path(request):
    return render(request, 'blog/recipe_path.html', {})

def upload_recipe_view(request):

    if request.method == 'POST':
        form = UploadRecipeForm(request.POST, request.FILES)
        
        if form.is_valid():
            spreadsheet = pd.read_excel(request.FILES['file'])
            
            for index, row in spreadsheet.iterrows():
                # Assuming columns in the spreadsheet match your model fields
                category, _ = Category.objects.get_or_create(name=row['category_name'])
                recipe = Recipe(
                    title=row['title'],
                    selling_price=row['selling_price'],
                    category=category
                )
                recipe.save()

                # Parsing and saving ingredients for the recipe
                ingredient_names = row['ingredients'].split(", ")
                for ingredient_name in ingredient_names:
                    ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
                    RecipeIngredient.objects.create(
                        recipe=recipe,
                        ingredient=ingredient,
                        quantity=row['quantity']  
                    )

            return redirect('some_view_name') 

    else:
        form = UploadRecipeForm()
    
    return render(request, 'upload_recipe.html', {'form': form})


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html',{'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe,pk=pk)
    return render(request, 'recipe_detail.html',{'recipe': recipe})

def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail',pk=recipe.pk)
    else:
        form = RecipeForm()
        return render(request, 'recipe_edit.html', {'form':form})
    
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_edit.html', {'form': form})


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')
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

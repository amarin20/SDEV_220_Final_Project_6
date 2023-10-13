from django.shortcuts import render
from django.utils import timezone
from .models import Recipe


def recipe_list(request):
    recipe_post = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Recipehub/recipe_list.html', {'recipe_post': recipe_post})


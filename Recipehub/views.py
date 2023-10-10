from django.shortcuts import render

def recipe_path(request):
    return render(request, 'blog/recipe_path.html', {})

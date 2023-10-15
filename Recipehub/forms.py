from django import forms
from .models import Recipe 

class UploadRecipeForm(forms.Form):
    file = forms.FileField()

class RecipeForm(forms.ModelForm):
    class meta:
        model = Recipe
        fields = ['title', 'sellung_price', 'category']
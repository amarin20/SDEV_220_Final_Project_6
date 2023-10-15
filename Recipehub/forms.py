from django import forms
from .models import Recipe 

class UploadRecipeForm(forms.Form):
    file = forms.FileField()

class RecipeForm(Forms.ModelForm):
    class meta:
        model = Recipe
        fields = ['title', 'sellung_price', 'category']
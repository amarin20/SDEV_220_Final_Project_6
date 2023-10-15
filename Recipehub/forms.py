from django import forms
from .models import Recipe, RecipeIngredient
from django.forms import inlineformset_factory

class UploadRecipeForm(forms.Form):
    file = forms.FileField()

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'selling_price', 'instructions', 'category',]



from django.db import models
from django.utils import timezone

class UnitChoices(models.TextChoices):
    TEASPOON = 'tsp', 'Teaspoon'
    TABLESPOON = 'tbsp', 'Tablespoon'
    CUP = 'cup', 'Cup'
    OUNCE = 'oz', 'Ounce'
    POUND = 'lb', 'Pound'
    FLUID_OUNCE = 'fl oz', 'Fluid Ounce'
    PINT = 'pint', 'Pint'
    QUART = 'quart', 'Quart'
    GALLON = 'gallon', 'Gallon'


class Category(models.Model):
    name = models.CharField(max_length=225)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=225)
    cost = models.FloatField()
    
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructions = models.TextField(default="No instructions provided.")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def profit_calculator(self):
        cost_price = 0
        recipe_indgredients = RecipeIngredient.objects.filter(recipe=self)

        for recipe_ingredient in recipe_indgredients:
            ingredient = recipe_ingredient.ingredient 
            quantity = float(recipe_ingredient.quantity)
            ingredient_cost = ingredient.cost
            cost_price += quantity * ingredient_cost

        profit = self.selling_price - cost_price
        formatted_profit = "{:.2f}".format(profit)
        return formatted_profit

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self): 
        return self.title
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50, choices=UnitChoices.choices, default=UnitChoices.OUNCE)

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()  # Step sequence
    step_description = models.TextField()
    



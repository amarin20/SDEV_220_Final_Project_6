from django.db import models

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

    def profit_calculator(self):
        cost_price = 0
        recipe_ingredients = RecipeIngredient.objects.filter(recipe=self)

        for recipe_ingredient in recipe_ingredients:
            ingredient_cost = recipe_ingredient.ingredient.cost
            quantity = float(recipe_ingredient.quantity)
            cost_price += quantity * ingredient_cost

        profit = self.selling_price - cost_price 
        return profit
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50, choices=UnitChoices.choices, default=UnitChoices.OUNCE)

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_number = models.PositiveIntegerField()  # Step sequence
    step_description = models.TextField()
    



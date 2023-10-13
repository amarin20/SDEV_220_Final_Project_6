from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=225)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=225)
    cost = models.FloatField()
    
class equipment(models.Model):
    name = models.CharField(max_length=225)
    
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructions = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def profit_calculator(self):

        cost_price = 0
        recipe_indgredients = RecipeIngredient.objects.filter(recipe=self)

        for recipe_ingredient in recipe_indgredients:
            ingredient = recipe_indgredients.ingredient 
            quantity = float(ingredient.quantity)
            ingredient_cost = Ingredient.cost
            cost_price += quantity * ingredient_cost

        profit = self.selling_price - cost_price 
        return profit 

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self): 
        return self.title
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)

class RecipeEquipment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    equipment = models.ForeignKey(equipment, on_delete=models.CASCADE)

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=225)
    
class ingredient(models.Model):
    name = models.CharField(max_length=225)
    cost = models.FloatField()
    
class  equipment(models.model):
    name = models.CharField(max_length=225)
    
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    selling_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructions = models.TextField()
    
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=255)

class RecipeEquipment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
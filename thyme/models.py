from django.db import models
from django.contrib.auth.models import User
 

class Family(models.Model):
  surname = models.CharField(max_length=30, primary_key=True) 
  
  def __str__(self):
    return self.surname

class FoodUser(models.Model):
  family = models.ForeignKey(Family, on_delete=models.CASCADE) 
  user = models.OneToOneField(User, on_delete=models.CASCADE)

class Timeline(models.Model):
  dishName = models.CharField(max_length=30, primary_key=True)
  family = models.ForeignKey(Family, on_delete=models.CASCADE)
  favorites = models.ManyToManyField(FoodUser)

class Recipe(models.Model):
  recipeName = models.TextField(max_length=30, primary_key=True)
  ingredients = models.TextField()
  directions = models.TextField()
  
class Timepoint(models.Model):
  date = models.DateField()
  story = models.TextField()
  recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
  author = models.OneToOneField(FoodUser, on_delete=models.CASCADE)
  timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
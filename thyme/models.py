from django.db import models
from django.contrib.auth.models import User
 
class Family(models.Model):
  surname = models.CharField(max_length=30, primary_key=True) 
  
  def __str__(self):
    return self.surname

class FoodUser(models.Model):
  family = models.ForeignKey(Family, on_delete=models.CASCADE) 
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.user.username

class Timeline(models.Model):
  # By default, Django gives each model the following field:
  # id = models.AutoField(primary_key=True)

  familyName = models.CharField(max_length=30, default='Default Family Name')
  dishName = models.CharField(max_length=30)
  family = models.ForeignKey(Family, on_delete=models.CASCADE)
  
#   favorites = models.ManyToManyField(FoodUser)
  def __str__(self):
    return  self.familyName + ' ' + self.dishName + ' Timeline'

class Recipe(models.Model):
  recipeName = models.TextField(max_length=30, primary_key=True)
  ingredients = models.TextField()
  directions = models.TextField()
  servings = models.IntegerField()
  prepTime = models.IntegerField()
  cookTime = models.IntegerField()
  
  
class Timepoint(models.Model):
  date = models.DateField()
  story = models.TextField()
  author = models.ForeignKey(FoodUser, on_delete=models.CASCADE)
  recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, blank=True, null=True)
  timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE, blank=True, null=True)
  
  def __str__(self):
    return "Date: " + str(self.date) + " | Story: " + self.story + " | ID: " + str(self.id)

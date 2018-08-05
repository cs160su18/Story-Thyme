from django.shortcuts import render, HttpResponse
from django.core import serializers
from thyme.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from .forms import RecipeForm

def index(request):
  return render(request, 'thyme/index.html')
  
def homepage(request):
  return render(request, 'thyme/homepage.html')

def searchresults(request):
  return render(request, 'thyme/searchresults.html')

def createnew(request):
  return render(request, 'thyme/createnew.html')

def namethymeline(request):
  return render(request, 'thyme/namethymeline.html')

def writerecipe(request):
  if request.method == 'POST':
    form = RecipeForm(request.POST)
    if form.is_valid():
      print("FORM IS VALID, HERE IS DATA:")
      print(form.cleaned_data) # testing for now
      recipe_name = form.cleaned_data['recipe_name']
      ingredients = form.cleaned_data['ingredients']
      directions = form.cleaned_data['directions']
      servings = form.cleaned_data['servings']
      prep_time = form.cleaned_data['prep_time']
      cook_time = form.cleaned_data['cook_time']
      
      # create a new Recipe and save it to Database (name, ingredients, directions for now)
      recipe = Recipe(recipeName =recipe_name, ingredients=ingredients, directions=directions)
      recipe.save()
  else:
    print("FORM IS NOT VALID!!!")
    form = RecipeForm()
  return render(request, 'thyme/writerecipe.html', {'form': form})

def addrecipe(request):
  return render(request, 'thyme/addrecipe.html')

def profile(request):
  return render(request, 'thyme/profile.html')

def family(request):
  return render(request, 'thyme/family.html')

def thymeline(request):
  return render(request, 'thyme/thymeline.html')

def mycontributedthymelines(request):
  return render(request, 'thyme/mycontributedthymelines.html')

# Process search for Timeline from homepage.html
def homepageSearchQuery(request):
    queryDishName = request.GET.get('dishName', None)
    dishNameExists = Timeline.objects.filter(dishName=queryDishName).exists()
    if dishNameExists:
      timelines = Timeline.objects.filter(dishName=queryDishName)
      obj = {}
      counter = 0
      for timeline in timelines:
          obj["timeline" + str(counter)] = helper(timeline)
          counter = counter + 1
      return JsonResponse(obj)
    else:
      # Timeline doesn't exist
      data = {
        'success': 'timeline_error'
      }
      return JsonResponse(data) 
  
def helper(timeline):
    data = {
      'success': 'true',
      'surname': timeline.family.surname
    }
    return data

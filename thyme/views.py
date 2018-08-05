from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
from thyme.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from .forms import RecipeForm, TimepointForm

def index(request):
  return render(request, 'thyme/index.html')
  
def homepage(request):
  print("Hello World! From homepage views.py")
  return render(request, 'thyme/homepage.html')

def searchresults(request, dishName=''):
  print("Hello World! From searchresults views.py")
  print("dishName: ", dishName)
  timelines = Timeline.objects.filter(dishName=dishName)
  print("timelines: ", Timeline.objects)
  print("timelines.filter: ", timelines)
  obj = {}
  data = {}
  obj['data'] = data
  counter = 0
  for timeline in timelines:
    data["timeline" + str(counter)] = helper(timeline)
    print(timeline.family.surname)
    counter = counter + 1
  print(timelines)
  print(obj)
  return render(request, 'thyme/searchresults.html', obj)

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
      
      # create a new Recipe and save it to Database
      recipe = Recipe(recipeName =recipe_name, ingredients=ingredients, directions=directions, servings=servings, prepTime = prep_time, cookTime = cook_time)
      recipe.save()
  else:
    print("FORM IS NOT VALID!!!")
    form = RecipeForm()
  return render(request, 'thyme/writerecipe.html', {'form': form})

def addrecipe(request):
  if request.method == 'POST':
    form = TimepointForm(request.POST)
    if form.is_valid():
      print("FORM IS VALID, HERE IS DATA:")
      print(form.cleaned_data) # testing for now
      date = form.cleaned_data['date']
      story = form.cleaned_data['story']
    
      # create a new Timepoint and save it to Database
      # TO DO: fill in the null fields e.g. the current user
      # TO DO: fill in the recipe (from next page) and timeline (from previous page)
      timepoint = Timepoint(date=date, story=story)
      timepoint.save()
  else:
    print("TIMEPOINT FORM IS NOT VALID!!!")
    form = TimepointForm()
  return render(request, 'thyme/addrecipe.html', {'form': form})

def profile(request):
  return render(request, 'thyme/profile.html')

def family(request):
  return render(request, 'thyme/family.html')

def thymeline(request):
  return render(request, 'thyme/thymeline.html')

def mycontributedthymelines(request):
  return render(request, 'thyme/mycontributedthymelines.html')


def viewrecipe(request):
  return render(request, 'thyme/viewrecipe.html')

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
#       'surname': timeline.family.surname
      'surname': timeline.familyName

    }
    return data


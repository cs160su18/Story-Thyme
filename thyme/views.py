from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
from thyme.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from .forms import RecipeForm, TimepointForm, TimelineForm

def index(request):
  return render(request, 'thyme/index.html')

## MARK: - Homepage and Search
  
def homepage(request):
  """Render homepage.html"""
  
  print("Hello World! From homepage views.py")
  return render(request, 'thyme/homepage.html')

    
# BEGIN - SEARCHING THYMELINES FROM HOMEPAGE 
def searchresults(request, dishName=''):
  """Render searchresults.html and display relevant results from queried dishName"""
  print("Hello World! From searchresults views.py")
  print("dishName: ", dishName)
  timelines = Timeline.objects.filter(dishName=dishName)
  obj = createSearchTimelinesDataObject(timelines)
  return render(request, 'thyme/searchresults.html', obj)

def createSearchTimelinesDataObject(timelines):
  obj = {}
  data = {}
  obj['data'] = data
  counter = 0
  for timeline in timelines:
    data["timeline" + str(counter)] = searchResultsHelper(timeline)
    counter = counter + 1
  return obj
  
def searchResultsHelper(timeline):
    data = {
      'success': 'true',
      'surname': timeline.family.surname,
      'display_text': str(timeline),
      'idString': str(timeline.id)
    }
    return data
# END - SEARCHING THYMELINES FROM HOMEPAGE 
  
# BEGIN - SELECT THYMELINE CODE
def selectthymeline(request):
  currentUser = request.user
  foodUser = FoodUser.objects.get(user=currentUser)
  foodUserFamilyName = foodUser.family.surname
  timelines = Timeline.objects.filter(familyName=foodUserFamilyName)
  obj = createSelectTimelinesDataObject(timelines)
  return render(request, 'thyme/selectthymeline.html', obj)

def createSelectTimelinesDataObject(timelines):
  obj = {}
  data = {}
  obj['data'] = data
  counter = 0
  for timeline in timelines:
    data["timeline" + str(counter)] = selectThymelineHelper(timeline)
    counter = counter + 1
  return obj

def selectThymelineHelper(timeline):
    data = {
      'success': 'true',
      'dishName': timeline.dishName,
      'display_text': str(timeline)
    }
    return data
# END - SELECT THYMELINE CODE

## MARK: - Creating Timelines, Timepoints, and Recipes

def addtoexisting(request, familyName=''):
  user = Timeline.objects.filter(FoodUser = user.username)
  print(user.username)
  timelines = Timeline.objects.filter(familyName=user.Family)
  obj = {}
  data = {}
  obj['data'] = data
  counter = 0
  for timeline in timelines:
    data["timeline" + str(counter)] = existingTimelinesHelper(timeline)
    counter = counter + 1
  return render(request, 'thyme/createnew.html', obj)
    
def existingTimelinesHelper(timeline):
    data = {
      'success': 'true',
      'surname': timeline.dishName
    }
    return data

def createthymeline(request):
  """Render createthymeline.html and create a new Timeline with dish name, family and family name."""
  
  if request.method == 'POST':
    form = TimelineForm(request.POST)
    if form.is_valid():
      dish_name = form.cleaned_data['dish_name']
      foodUser = FoodUser.objects.filter(user=request.user)[0] 
      family = foodUser.family
      timeline = Timeline(familyName=family.surname, 
                          dishName=dish_name, 
                          family=family)
      timeline.save()
  else:
    form = TimelineForm()
        
  return render(request, 'thyme/createthymeline.html', {'form': form})

def addtimepoint(request, dishName=''): 
  """Render addtimepoint.html, save a new Timepoint and render the Add Timepoint view"""
  
  if request.method == 'POST':
    form = TimepointForm(request.POST)
    if form.is_valid():
      date = form.cleaned_data['date']
      story = form.cleaned_data['story']
      
      foodUser = FoodUser.objects.get(user=request.user)
      foodUserFamilyName = foodUser.family.surname;
      timeline = Timeline.objects.get(familyName=foodUserFamilyName, dishName=dishName);
      timepoint = Timepoint(date=date, story=story, author=foodUser, timeline=timeline);
      print(timeline);
      # TO DO: fill in the Timeline field of Timepoint with info from previous page     
      timepoint.save()
  else:
    form = TimepointForm()
  return render(request, 'thyme/addtimepoint.html', {'form': form})

def writerecipe(request):
  """Render writerecipe.html and save a new Recipe"""
    
  print("HelloWorld! from writerecipe.")
  if request.method == 'POST':
    form = RecipeForm(request.POST)
    if form.is_valid():
      print("recipe form is valid")
      recipe_name = form.cleaned_data['recipe_name']
      ingredients = form.cleaned_data['ingredients']
      directions = form.cleaned_data['directions']
      servings = form.cleaned_data['servings']
      prep_time = form.cleaned_data['prep_time']
      cook_time = form.cleaned_data['cook_time']
      
      recipe = Recipe(recipeName=recipe_name, 
                      ingredients=ingredients, 
                      directions=directions, 
                      servings=servings, 
                      prepTime=prep_time, 
                      cookTime=cook_time)
      recipe.save()           
      foodUser = FoodUser.objects.filter(user=request.user)[0] 
      
      # save recipe to latest time point created by this user
      latestTimePoint = Timepoint.objects.filter(author=foodUser).order_by('-date')[0]
      latestTimePoint.recipe = recipe
      latestTimePoint.save() 
  else:
    form = RecipeForm()
  return render(request, 'thyme/writerecipe.html', {'form': form})

# def addtimepoint(request): 
#   """ Save a new Timepoint and render the Add Timepoint view"""
#   print("add timepoint being called")
#   if request.method == 'POST':
#     print("timepoint form is valid")
#     form = TimepointForm(request.POST)
#     if form.is_valid():
#       date = form.cleaned_data['date']
#       story = form.cleaned_data['story']
    
#       # create a new Timepoint and save it to Database
#       foodUser = FoodUser.objects.filter(user=request.user)[0]
#       timepoint = Timepoint(date=date, story=story, author=foodUser)  
#       # TO DO: fill in the Timeline field of Timepoint with info from previous page     
#       timepoint.save()
#   else:
#     form = TimepointForm()
#   return render(request, 'thyme/addtimepoint.html', {'form': form})



## MARK: - Viewing Timelines and Recipes




def thymeline(request, thymelineId):
  print("from thymeline in views.py")
  # to do: offer protection if none exists
  timeline = Timeline.objects.filter(id=thymelineId)[0] 
  timepoints = Timepoint.objects.filter(timeline=timeline).order_by('date')
  print("timepoints for timeline with id", thymelineId, "are ", timepoints)
#   obj['data'] = data

  data = {}
  data['timeline'] = str(timeline)
  data['timepoints'] = timepoints
#   for timepoint in timepoints:
#     data[str(timepoint.id)] = timepoint
    
  print("data", data)
  
  # also extract all timepoints, their dates and stories
  return render(request, 'thyme/thymeline.html', data)


 

def viewrecipe(request,timepointId):
  timepoint = Timepoint.objects.filter(id=timepointId)[0]      
  recipe = timepoint.recipe
  data = {}
  data['recipe'] = recipe
  return render(request, 'thyme/viewrecipe.html', data)  

## MARK: - User Profile, Family, and Contribution pages

def profile(request):
  return render(request, 'thyme/profile.html')

def family(request):
  print("family request from views.py")
  data = {}
  data['firstName'] = request.user.first_name # does presume there is a first and last name!
  data['lastName'] = request.user.last_name
  print("First and last name", data['firstName'], data['lastName'])
  
  family = FoodUser.objects.get(user=request.user).family
  print("Family", family)
  
  familyTimelines = Timeline.objects.filter(family=family)
  data['timelines'] = familyTimelines
  print("family timelines", familyTimelines)

  members = FoodUser.objects.filter(family=family)
  data['members'] = members
  print("family members", members)
  return render(request, 'thyme/family.html', data)

def mycontributedthymelines(request):
  foodUser = FoodUser.objects.get(user=request.user)
  print("!! user is:", request.user, " food user: ", foodUser)
  timepoints = Timepoint.objects.filter(author=foodUser)
  timelines = set([tp.timeline for tp in timepoints if tp.timeline is not None]) 
  print("timelines", timelines)
  
  return render(request, 'thyme/mycontributedthymelines.html', {'timelines': timelines})

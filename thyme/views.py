from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
from thyme.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from .forms import RecipeForm, TimepointForm, TimelineForm

def index(request):
  return render(request, 'thyme/index.html')
  
def homepage(request):
  print("Hello World! From homepage views.py")
  return render(request, 'thyme/homepage.html')

def searchresults(request, dishName=''):
  print("Hello World! From searchresults views.py")
  print("dishName: ", dishName)
  timelines = Timeline.objects.filter(dishName=dishName)
  obj = createTimelinesDataObject(timelines)
#   obj = {}
#   data = {}
#   obj['data'] = data
#   counter = 0
#   for timeline in timelines:
#     data["timeline" + str(counter)] = helper(timeline)
#     print(timeline.family.surname)
#     counter = counter + 1
#   print(timelines)
#   print(obj)
  return render(request, 'thyme/searchresults.html', obj)

def createTimelinesDataObject(timelines):
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
  return obj

def helper(timeline):
    data = {
      'success': 'true',
      'surname': timeline.family.surname
    }
    return data


def showTimelinesDataObject(timelines):
  obj = {}
  data = {}
  obj['data'] = data
  counter = 0
  for timeline in timelines:
    data["timeline" + str(counter)] = helperShowThymeline(timeline)
    print(timeline.dishName)
    counter = counter + 1
  print(timelines)
  print(obj)
  return obj

def helperShowThymeline(timeline):
    data = {
      'success': 'true',
      'dishName': timeline.dishName
    }
    return data

def selectthymeline(request):
  currentUser = request.user
  foodUser = FoodUser.objects.get(user=currentUser)
  foodUserFamilyName = foodUser.family.surname
  timelines = Timeline.objects.filter(familyName=foodUserFamilyName)
  print(timelines)
  obj = showTimelinesDataObject(timelines)
  print(obj)
  return render(request, 'thyme/selectthymeline.html', obj)

def createNewThymeline(request):
    print("Hello World! from createNewThymeline.")
    if request.method == "POST":
      newThymelineData = json.loads(request.body.decode('ASCII'))
      thymelineName = newThymelineData['thymelineName']
      familyName = newThymelineData['familyName']
      family = Family.objects.get(surname=familyName)
      Timeline(familyName, thymelineName, family).save()
      return HttpResponse("")
    else:
      return render(request, 'thyme/namethymeline.html')

def namethymeline(request):
    print("Hello World! from createNewThymeline.")
    if request.method == "POST":
      newThymelineData = json.loads(request.body.decode('ASCII'))
      thymelineName = newThymelineData['thymelineName']
      familyName = newThymelineData['familyName']
      family = Family.objects.get(surname=familyName)
      Timeline(familyName, thymelineName, family).save()
      return HttpResponse("")
    else:
      return render(request, 'thyme/namethymeline.html')
    
def createthymeline(request):
  if request.method == 'POST':
    print("create timeline post request")
    form = TimelineForm(request.POST)
    if form.is_valid():
      print("timeline form is valid")
      dish_name = form.cleaned_data['dish_name']
      foodUser = FoodUser.objects.filter(user=request.user)[0] 
      print("user is", foodUser)
      family = foodUser.family
      print("family is", family)
      timeline = Timeline(familyName=family.surname, dishName=dish_name, family=family)
      print("timeline is", timeline)
      timeline.save()
  else:
    form = TimelineForm()
        
  return render(request, 'thyme/createthymeline.html', {'form': form})

def writerecipe(request):
  """ Save a new Recipe and render the Write Recipe view"""  
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
      
      # create a new Recipe and save it to Database
      recipe = Recipe(recipeName=recipe_name, 
                      ingredients=ingredients, 
                      directions=directions, 
                      servings=servings, 
                      prepTime=prep_time, 
                      cookTime=cook_time)
      recipe.save()
           
      # debugging note: the logged in User must be associated with a FoodUser manually (through admin)
      foodUser = FoodUser.objects.filter(user=request.user)[0] 
      
      # save recipe to latest time point created by this user
      latestTimePoint = Timepoint.objects.filter(author=foodUser).order_by('-date')[0] # order by date descending
      latestTimePoint.recipe = recipe
      latestTimePoint.save()            
  else:
    form = RecipeForm()
  return render(request, 'thyme/writerecipe.html', {'form': form})

def addtimepoint(request): 
  """ Save a new Timepoint and render the Add Timepoint view"""
  print("add timepoint being called")
  if request.method == 'POST':
    print("timepoint form is valid")
    form = TimepointForm(request.POST)
    if form.is_valid():
      date = form.cleaned_data['date']
      story = form.cleaned_data['story']
    
      # create a new Timepoint and save it to Database
      foodUser = FoodUser.objects.filter(user=request.user)[0]
      timepoint = Timepoint(date=date, story=story, author=foodUser)  
      # TO DO: fill in the Timeline field of Timepoint with info from previous page     
      timepoint.save()
  else:
    form = TimepointForm()
  return render(request, 'thyme/addtimepoint.html', {'form': form})

def profile(request):
  return render(request, 'thyme/profile.html')

def family(request):
  currentUser = request.user
  foodUser = FoodUser.objects.get(user=currentUser)
  foodUserFamilyName = foodUser.family.surname
  print(foodUserFamilyName)
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
    
def addtoexisting(request, familyName=''):
  user = Timeline.objects.filter(FoodUser = user.username)
  print(user.username)
  timelines = Timeline.objects.filter(familyName=user.Family)
  obj = {}
  data = {}
  obj['data'] = data
  counter = 0
  for timeline in timelines:
    data["timeline" + str(counter)] = helperDish(timeline)
    counter = counter + 1
  return render(request, 'thyme/createnew.html', obj)

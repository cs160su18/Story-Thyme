from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
from thyme.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse

def index(request):
  return render(request, 'thyme/index.html')
  
def homepage(request):
  print("Hello World! From homepage views.py")
  return render(request, 'thyme/homepage.html')

def searchresults(request, dishName=''):
  print("Hello World! From searchresults views.py")
  print("dishName: ", dishName)
  timelines = Timeline.objects.filter(dishName=dishName)
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
  return render(request, 'thyme/writerecipe.html')

def addrecipe(request):
  return render(request, 'thyme/addrecipe.html')
  
def helper(timeline):
    data = {
      'success': 'true',
      'surname': timeline.family.surname
    }
    return data
  
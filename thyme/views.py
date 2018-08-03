from django.shortcuts import render, HttpResponse
from django.core import serializers
from thyme.models import *
from django.core.serializers import serialize
import json
from django.http import JsonResponse

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

# Process search for Timeline from homepage.html
def homepageSearchQuery(request):
    queryDishName = request.GET.get('dishName', None)
    dishNameExists = Timeline.objects.filter(dishName=queryDishName).exists()
    if dishNameExists:
      timeslines = Timeline.objects.filter(dishName=queryDishName)
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
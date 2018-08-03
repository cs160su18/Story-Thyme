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
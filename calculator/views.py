from django.shortcuts import render
from django.http import HttpResponse
from .models import food

# Create your views here.

def index(request):
  foods = food.objects.all
  context = {'foods': foods}
  return render(request, 'calculator/index.html', context)

def result(request):
  return render(request, 'calculator/result.html')

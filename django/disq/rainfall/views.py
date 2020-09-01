from django.shortcuts import render
from django.http import HttpResponse, response
import pandas as pd
import csv

# Create your views here.
def home(request):
    return render(request, 'home.html')

def graph(request):
    return render(request, 'graph.html')

def predict(request):
    return render(request, 'predict.html')
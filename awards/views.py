from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt



# Create your views here.
def home(request):
    return render(request, 'home.html')

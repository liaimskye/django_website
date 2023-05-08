from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request,'landing.html')

def home_page(request):
    return render(request,'home.html')

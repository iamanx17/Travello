from django.shortcuts import render
from .models import destination
# Create your views here.

def home(request):
    dest=destination.objects.all()
    return render(request,'index.html',{'dest':dest})

def blog(request):
    return render(request,'news.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
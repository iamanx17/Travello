from django.shortcuts import render,redirect
from .forms import user

# Create your views here.

def register(request):
    form=user(request.POST)
    if form.is_valid():
        form.save()
        print(request.POST)
        return redirect('/')
    return render(request,'register.html',{'form':form})

def login(request):
    return render(request, 'login.html')

def info(request):
    return render(request,'info.html')
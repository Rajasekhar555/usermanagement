from django.shortcuts import render

from .models import UserData

def home(request):
    context={
        "content":"USER MANAGEMENT SYSTEM"
    }
    return render(request,'base.html',context)


def register(request):
    return render(request,'new_registration.html')

def login(request):
    return render(request,'login.html')

def edit_register(request):
    return render(request,'edit_registration.html')

def delete_register(request):
    return render(request,'delete_registration.html')
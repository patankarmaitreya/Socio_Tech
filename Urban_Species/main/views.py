from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def assist(request):
    return render(request, "main/assist.html")

def adopt(request):
    return render(request, "main/adopt.html")

def medic(request):
    return render(request, "main/medic.html")

def help(request):
    return render(request, "main/help.html")
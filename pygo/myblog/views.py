from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def layout (request):
    return render(request,"layout_homepage.html")

def homepage (request):
    rating = 4
    testrunlist = ["test01_usingloop","test02_usingloop","test03_usingloop"]
    return render(request,"homepage.html",{'testrunlist':testrunlist,"rating":rating})

def page1 (request):
    sword = ['Wood sword','Iron sword','Gold sword','Platinum sword','Diamond sword','Legendary sword']
    return render(request, "page1.html",{"sword":sword})



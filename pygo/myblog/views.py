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

def community (request):
    return render(request, "community_form_get.html")

def addget(request):
    a = request.POST["part1"]
    b = request.POST["part2"]
    return render((request), "addform.html",{"p1" : a,"p2" : b})



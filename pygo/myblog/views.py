from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def layout(request):
    return render(request,"layout_homepage.html")

def homepage (request):
    rating = 3
    testrunlist = ["test01","test02","test03"]
    return render(request,"homepage.html",{'testrunlist':testrunlist,"rating":rating})



from django.shortcuts import render,redirect 
from django.http import HttpResponse
from myblog.models import community_post
from django.contrib.auth.models import User


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

def using_object(request):
    build = community_post.objects.all
    return render(request, "object.html",{"data":build})

def register(request):
    return render(request, "register.html")

def com_register(request):
    username = request.POST["user"]
    password = request.POST["Password"]
    repassword = request.POST["re_Password"]
    firstname = request.POST["First_Name"]
    lastname = request.POST["Last_Name"]
    email = request.POST["Email"]

    if password == repassword :
        if User.objects.filter(username=username).exists():
            print("User exists")
            return redirect("/register")
        elif User.objects.filter(email=email).exists():
            print("Email exists")
            return redirect("/register")
        else:    
            user=User.objects.create_user(
            username=username,
            password=password,
            first_name=firstname,
            last_name=lastname,
            email=email
        )
            user.save()
            print("Register Complete")
            return redirect("/home")
    else:
        return redirect("/register")





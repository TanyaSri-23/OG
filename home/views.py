from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):


    return render(request, 'index.html')
    # return HttpResponse("This is a test response for the Home page.")


def about(request):
    return render(request, 'about.html')
# def about(request):
#     return HttpResponse("This is a test response for the About page.")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        contact=Contact(name=name, email=email,phone=phone, desc=desc, date=datetime.now())
        contact.save()
        messages.success(request, "Thanks! Your Message has been sent.")

    return render(request, 'contact.html')

def service(request):
   
    return render(request, 'service.html')

def loginUser(request):
    if request.method=="POST":
        # check if user crediantials is true
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            
            messages.success(request, "Sucessfully Logged in")
            login(request,user)
            return redirect("/")
 
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    return redirect('/login')





from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .models import RegisterForm

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login') 
    return render(request, 'home/index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request,"Succesful Logged-In")
            return redirect("/")

        else:
            # No backend authenticated the credentials
            messages.error(request,"Invalid Credentials ,Please Try Again")
            return render(request, 'home/login.html')

    return render(request, 'home/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request,"Succesful Logout")

    return redirect("/login")

def about(request):
    return render(request, 'home/about.html') 


def test(request):
    return render(request, 'home/test.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'home/contact.html')
def register(request):
    if request.method == 'POST':
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have been registered')
        return redirect("/login")
    else:
        form=RegisterForm()
        messages.warning(request, 'Fill all the field')

        
    
    return render(request, 'home/register.html', {"form":form})

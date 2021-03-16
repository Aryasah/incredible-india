from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login ,get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings





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
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            
            current_site = get_current_site(request)
            mail_subject = 'Welcome To Incredible India'
            message = render_to_string('home/acc_active_email.html')
            print(message)
            to_email = form.cleaned_data.get('email')
            send_mail(
                        mail_subject,
                        message,
                        settings.EMAIL_HOST_USER ,
                        [to_email],                      
            )
            print(to_email)
            messages.success(request, 'Your message has been sent!')
            
            
            user.save()
            return render(request,'home/acc_active_sent.html')
    else:
        form = SignupForm()
    return render(request, 'home/signup.html', {'form': form})


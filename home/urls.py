
from django.urls import path
from django.contrib import admin
from . import views
from home import views
from django.conf.urls import url,include
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'), 
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    
    url(r'^signup/$', views.signup, name='signup'),

    


]

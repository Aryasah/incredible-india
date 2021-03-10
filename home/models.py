from django.db import models
from django.contrib.auth import logout, authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class RegisterForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
      
    
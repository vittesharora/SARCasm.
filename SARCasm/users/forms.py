from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	roll=forms.CharField(max_length=9)
	class Meta:
		model=User
		fields=['username','email','roll','password1','password2']
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Player

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	roll=forms.CharField(max_length=9)

	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		# Making name required
		self.fields['email'].required = True
		# self.fields['first_name'].required = True

	class Meta:
		model=User
		fields=['username', 'first_name', 'last_name','email','roll','password1','password2'] 
		#first_name and last_name added just for convenience

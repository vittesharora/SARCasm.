from django.urls import path
from .import views

urlpatterns=[
	path('',views.home, name='game-home'),
	path('play',views.play, name='play'),
	path('prize',views.prize, name='prize'),
	
]
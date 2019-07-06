from django.urls import path
from .import views
from .views import Play

urlpatterns=[
	path('',views.home, name='game-home'),
	path('play',Play.as_view(), name='play'),
	path('prize',views.prize, name='prize'),
]
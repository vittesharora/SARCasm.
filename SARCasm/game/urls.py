from django.urls import path
# from django.views.generic import TemplateView
from .import views
from .views import Play

urlpatterns=[
	path('',views.home, name='game-home'),
	path('play',Play.as_view(), name='play'),
	# path('play',views.play, name='play'),
]
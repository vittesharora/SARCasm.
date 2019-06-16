from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request, 'game/home.html',{})

@login_required
def play(request):
	return render(request, 'game/play.html',{})
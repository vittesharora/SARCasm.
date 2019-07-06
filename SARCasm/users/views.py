from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import userdata

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            referral=form.cleaned_data.get('referral')
            if userdata.objects.filter(roll=referral).exists():
                t=userdata.objects.get(roll=referral)
                if t.referral_count<3:
                    t.referral_count=t.referral_count+1
                t.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
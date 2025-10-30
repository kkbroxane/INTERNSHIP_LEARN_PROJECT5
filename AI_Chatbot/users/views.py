from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.storage import FileSystemStorage
from django.utils.text import get_valid_filename
from django.contrib import messages
from django.conf import settings
import os

from .forms import UserRegistrationForm
from .models import *
from message.views import *

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect email or password.')

    return render(request, 'login.html')

def register(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login_page')

    return render(request, 'register.html', {'form': form})

@login_required
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST' and request.FILES.get('profile_pic'):
        profile_pic = request.FILES['profile_pic']
        user = request.user
        filename = get_valid_filename(os.path.basename(profile_pic.name))
        fs = FileSystemStorage()
        saved_name = fs.save(filename, profile_pic)
        user.profile_pic.name = saved_name
        user.save()
        return redirect('user_profile')
    return redirect('user_profile')

from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import student, Profile
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    return render(request, "index.html", {'student': student.objects.all()})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']

        if password != cpassword:
            messages.error(request, "Password does not match")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request,user_login)
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, user_id = user_model.id)
            new_profile.save()
            return redirect('signup')
    return render(request, "signup.html")
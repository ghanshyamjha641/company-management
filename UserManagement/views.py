from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Optional, for flash messages



# Create your views here.
def index(request):
    return HttpResponse("hello this is demo data!")

#Signup page.
def user_signup(request):
    if request.method == 'POST':
        form = request.POST
        fullname = form.get('fullname')
        username = form.get('email')
        email = form.get('email')
        password = form.get('password')
        confirmpassword = form.get('confirmpassword')
        phone = form.get('phone')

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email is already registered'})

        #check the password match
        if password!=confirmpassword:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        
        # If any field is empty, return an error
        if not all([username, email, password, phone]):
            return render(request, 'signup.html', {'error': 'All fields are required'})

        user_obj = CustomUser(first_name=fullname, username=username, email=email, phone=phone, password=make_password(password))

        user_obj.save()
        return redirect('login')

    return render(request,"signup.html")


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Check if all fields are filled
        if not email or not password:
            return render(request, 'login.html', {'error': 'Email and password are required'})

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL name after login
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
        

    return render(request,'login.html')

#Home Page
def home(request):
    return render(request,'home.html')

#logout
def user_logout(request):
    logout(request)
    return redirect('login')


#Edit Profile
# @login_required
def edit_profile(request):
    # render edit form or process POST
    return render(request, 'edit_profile.html')
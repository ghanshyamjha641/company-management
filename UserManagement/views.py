from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("hello this is demo data!")

#Signup page.
def admin_signup(request):
    return render(request,"signup.html")



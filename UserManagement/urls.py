from django.urls import path
from . import views

urlpatterns =[
    path("index", views.index, name="index"),
    path("signup/", views.user_signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path("home/", views.home, name="home"),
    path('logout/', views.user_logout, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
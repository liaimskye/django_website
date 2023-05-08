from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('user_authenticate', views.user_authenticate, name="authenticate"),
    path('login/', views.user_login, name="login"),
    path('register/', views.register, name= 'register'),
    path('logout/', views.log_out, name="logout")
]

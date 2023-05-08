from django.contrib import admin
from django.urls import path, include
from . import views

appname= 'base'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('landing', views.landing_page, name='landing')
]

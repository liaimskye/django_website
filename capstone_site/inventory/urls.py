from django.contrib import admin
from django.urls import path, include
from . import views

appname= 'inventory'

urlpatterns = [
    path('Query/', views.query_create, name="create_query")
]

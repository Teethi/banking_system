from django import views
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout')
]
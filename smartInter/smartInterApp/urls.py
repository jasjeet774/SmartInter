from django.contrib import admin
from django.urls import path
from . import views
# app_name='SmartInterApp'
urlpatterns = [
    
    path('',views.Signup,name='signup'),
    path('login/',views.userlogin,name='userlogin'),
    path('home',views.home,name='home'),
    path('logout',views.userlogout,name='logout'),

   
]

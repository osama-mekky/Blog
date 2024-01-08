from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('login/',views.login_page, name='login'),
    path('register/',views.register_pasge, name='register'),
    path('logout/',views.logout_page, name='logout'),    
    path('profile<int:pk>/',views.profile , name='profile')
   
    
]
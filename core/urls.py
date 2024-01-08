from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('post/<int:pk>',views.post,name='post'),
   path('add_post/',views.add_Post,name='add_post'),
   path('delate_comment<int:pk>/',views.delate_comment , name='delate_comment'),
   path('delate_post<int:pk>/',views.delate_post , name='delate_post'),
   path('update_post<int:pk>',views.UpdatePost,name='update')



    
]

from django.shortcuts import render , redirect
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required


from .forms import *
# Create your views here.








def register_pasge(request):

   if request.user.is_authenticated:
        return redirect('home')
   else :
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            conf_password = request.POST['conf-password']

            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Is Taken')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'This Email is Already taken')
                else :
                    patt= "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
                    if re.match(patt,email):
                                if re.match(password,conf_password):
                                    user = User.objects.create_user(email=email,username=username,password=password)
                                    user.save()
                                    messages.success(request,'account Created Success')
                                    return redirect('login')
                                    
                                else:
                                    messages.error(request,"Password Not Match")

                    else :
                                messages.error(request,"Inavailed Email")






        return render(request,'accounts/Register.html') 



def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)

        if user is not None :
            auth.login(request,user)
            return redirect('home')
        else :
            messages.error(request,'email or password is in Vaild')


    return render(request,'accounts/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login') 


@login_required(login_url='login')
def profile(request , pk):
     user = User.objects.get(id = pk)
     form = UserForm(instance=user)
     if request.method == 'POST':
          form = UserForm(request.POST , instance=user)
          if form.is_valid():
               form.save()
               messages.success(request , 'Save Changes Done')
               return redirect('profile',pk = user.id)
     return render(request , 'accounts/profile.html',{'form':form})
     
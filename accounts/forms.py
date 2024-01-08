from django.forms import ModelForm

from .models import *
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta :
        model = User
        fields = ['username', 'email','first_name' , 'last_name']

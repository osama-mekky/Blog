from django import forms
from.models import *
from django.forms import ModelForm
class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = '__all__'
        exclude = ['user',]
        widgets = {
            'tilte' :forms.TextInput(attrs={'class':'form-control'}),
            'category' :forms.Select(attrs={'class':'form-control'}),
            'text' :forms.Textarea(attrs={'class':'form-control'}),
            'photo' :forms.FileInput(attrs={'class':'form-control'}),

        }

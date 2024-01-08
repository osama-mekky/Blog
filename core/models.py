from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL , null=True)
    tilte = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL , null=True)
    text = RichTextField(null=True ,  blank=True)
    photo = models.ImageField(null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.tilte


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['-update','-created_at']

    def __str__(self):
        return self.body[0:50]    


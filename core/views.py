from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from django.db.models import   Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


def home(request):
   

    q= request.GET.get('q') if request.GET.get('q') != None else ""
    posts = Post.objects.filter(Q(tilte__icontains = q))
    
    return render(request, 'home.html',{'posts':posts})




def post(request,pk):
    post = Post.objects.get(id = pk)
    post_comments = post.comment_set.all()

    if request.method == 'POST':
        message = request.POST['body']
        comment = Comment.objects.create(user = request.user , post = post , body = message)
        return redirect('post',pk = post.id)
        

    return render(request , 'post.html',{"post":post, 'post_comments':post_comments})

@login_required(login_url='login')
def add_Post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request , 'The Post Was Add Successfuly')
            



    return render(request , 'add_post.html',{'form':form})

@login_required(login_url='login')
def delate_post(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    messages.success(request, 'the Post is Delateed')
    return redirect('home')


@login_required(login_url='login')
def delate_comment(request , pk):
    comment = Comment.objects.get(id= pk)
    comment.delete()
    return redirect('post', pk = comment.post.id)

@login_required(login_url='login')
def UpdatePost(request , pk):
    post = Post.objects.get(id = pk)
    form = PostForm(instance=post)

    if request.user != post.user :
        return HttpResponse("Not Allowd Of You")
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"the post was Updated")
            return redirect('post',pk=post.id)
    context = {'form':form}
    return render (request,'update.html',context)    

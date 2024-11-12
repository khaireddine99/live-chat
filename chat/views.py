# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import PostForm, CommentForm
from chat.models import Post, Comment, Screenshot
from django.conf import settings
import requests
import base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
 
@login_required
def index(request):
    return render(request, "index.html")

@login_required
def room(request, room_name):
    current_user = request.user
    username = current_user.username
    data = {
        "room_name": room_name ,
        "user_name": username
    }
    return render(request, "room.html", {"data": data})

# custom login view --------------------------------------------------
def customLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("user logged in")
            return redirect('index')
            
        else:
            print("user not found")    

    return render(request, 'customLogin.html')       


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('posts')
        else:
            form.add_error(None, 'Invalid reCAPTCHA. Please try again.')
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})

# Fetch all posts from the database
def post_list(request):
    posts = Post.objects.all()  
    return render(request, 'posts.html', {'posts': posts})

# fetch a post 
def post(request, post_id):
    post = Post.objects.get(id=post_id)

    # load comments
    comments = Comment.objects.filter(post=post)

    # write a comment 
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            NewComment = form.save(commit=False)
            NewComment.post = post
            NewComment.save()
            form = CommentForm   
        else:
            form.add_error(None, 'Invalid reCAPTCHA. Please try again.') 

    context = {'post':post, 'form': form, 'comments':comments }
    return render(request, 'post.html', context)

def audio_post(request):
    return render(request, 'audio_post.html')


def capture_view(request):
    return render(request, 'cam.html')


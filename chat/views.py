# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import PostForm
from chat.models import Post
 

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
        
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})

# Fetch all posts from the database
def post_list(request):
    posts = Post.objects.all()  
    return render(request, 'posts.html', {'posts': posts})

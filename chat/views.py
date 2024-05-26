# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
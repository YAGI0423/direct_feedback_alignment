from django.shortcuts import render

# Create your views here.
from .models import GameRoom

def gameRoom(request):
    return render(
        request,
        'gameRoom/index.html'
    )

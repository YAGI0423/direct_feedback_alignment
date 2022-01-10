from django.shortcuts import render

# Create your views here.
from .models import GameRoom

def gameRoom(request, pk):
    roomInfo = GameRoom.objects.get(pk=pk)

    return render(
        request,
        'gameRoom/index.html',
        {
            'roomInfo': roomInfo,
        }
    )

from django.shortcuts import render

# Create your views here.
from .models import LiveRoom

def index(request):
    liveRooms = LiveRoom.objects.all().order_by('-pk')

    return render(
        request,
        'lobby/index.html',
        {
            'liveRooms': liveRooms,
        }
    )

def room_page(request, pk):
    roomInfo = LiveRoom.objects.get(pk=pk)

    return render(
        request,
        'lobby/gameRoom.html',
        {
            'roomInfo': roomInfo,
        }
    )

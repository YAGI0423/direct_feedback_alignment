from django.shortcuts import render

# Create your views here.
from .models import RoomList

def index(request):
    liveRooms = RoomList.objects.all().order_by('-pk')

    return render(
        request,
        'lobby/index.html',
        {
            'liveRooms': liveRooms,
        }
    )

def room_page(request, pk):
    roomInfo = RoomList.objects.get(pk=pk)

    return render(
        request,
        'lobby/gameRoom.html',
        {
            'roomInfo': roomInfo,
        }
    )

from django.shortcuts import render


# Create your views here.
from .models import RoomList


def roomList(request):
    roomInfo = RoomList.objects.all().order_by('-pk')
    return render(
        request,
        'lobby/index.html',
        {
            'roomInfo': roomInfo,
        }
    )

def gameRoom(request, pk):
    roomInfo = RoomList.objects.get(pk=pk)
    return render(
        request,
        'lobby/room.html',
        {
            'roomInfo': roomInfo,
        }
    )

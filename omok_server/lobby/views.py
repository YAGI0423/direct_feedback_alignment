from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView   #목록 생성
from .models import RoomList

class RoomList(ListView):
    model = RoomList
    ordering = '-pk'
    template_name = 'lobby/index.html'

def gameRoom(request, pk):
    roomInfo = RoomList.objects.get(pk=pk)

    return render(
        request,
        'lobby/room.html',
        {
            'roomInfo': roomInfo,
        }
    )

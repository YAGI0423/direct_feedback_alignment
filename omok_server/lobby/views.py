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

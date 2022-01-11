# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView   #목록 생성
from .models import RoomList

class RoomList(ListView):
    model = RoomList
    ordering = '-pk'
    template_name = 'lobby/index.html'

# def index(request):
#     liveRooms = RoomList.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'lobby/index.html',
#         {
#             'liveRooms': liveRooms,
#         }
#     )

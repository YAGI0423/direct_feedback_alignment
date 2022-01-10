from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomList.as_view()),
]

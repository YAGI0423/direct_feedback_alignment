from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomList.as_view()),
    path('<int:pk>/', views.gameRoom),   #int값을 pk변수로 반환
]

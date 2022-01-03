from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.room_page),   #int값을 pk변수로 반환
]

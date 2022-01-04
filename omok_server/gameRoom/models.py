from django.db import models

# Create your models here.
class GameRoom(models.Model):
    roomName = models.CharField(max_length=30)
    hostName = models.CharField(max_length=10)
    gameStatus = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

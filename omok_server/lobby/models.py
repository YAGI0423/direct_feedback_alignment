from django.db import models

# Create your models here.
class LiveRoom(models.Model):
    roomName = models.CharField(max_length=30)
    hostName = models.CharField(max_length=10)
    gameStatus = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}] {self.roomName} ({self.hostName})'


    def get_absolute_url(self):
        return f'/lobby/{self.pk}/'

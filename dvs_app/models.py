from django.db import models

# Create your models here.
class ClientInteractionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    client_ip = models.CharField(max_length=100)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.timestamp} - {self.client_ip} - {self.action}'

class BroadcastingInfo(models.Model):
    broadcast_time = models.DateTimeField()
    timezone = models.CharField(max_length=100)
    video_filename = models.CharField(max_length=255)
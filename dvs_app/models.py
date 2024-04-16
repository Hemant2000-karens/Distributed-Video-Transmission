from django.db import models
from django.utils import timezone
import pytz


# Create your models here.
class ClientInteractionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    client_ip = models.CharField(max_length=100)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.timestamp} - {self.client_ip} - {self.action}'


class ApplicationLog(models.Model):
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

# class BroadcastingInfo(models.Model):
#     broadcast_time = models.DateTimeField()
#     timezone = models.CharField(max_length=100)
#     video_filename = models.CharField(max_length=255)

class BroadcastingInfo(models.Model):
    broadcast_time = models.DateTimeField()
    timezone = models.CharField(max_length=100)
    video_filename = models.CharField(max_length=255)
    viewers_count = models.IntegerField(default=0)
    video_id = models.CharField(max_length=100, unique=True, default='0V')

    def __str__(self):
        return f"Broadcast at {self.broadcast_time}"

class ServerTimeZone(models.Model):
    server_name = models.CharField(max_length=100)
    TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
    timezone = models.CharField(max_length=100, choices=TIMEZONE_CHOICES)

    def __str__(self):
        return self.server_name
from django.db import models
from django.utils import timezone
import pytz


class ClientInteractionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    client_ip = models.GenericIPAddressField()
    action = models.CharField(max_length=255)
    username = models.CharField(max_length=150, null=True, blank=True)
    server_id = models.IntegerField(default=1)  # Add this field

    def __str__(self):
        return f'{self.timestamp} - {self.client_ip} - {self.action} - {self.username} - {self.server_id}'


# Create your models here.
# class ClientInteractionLog(models.Model):
#     timestamp = models.DateTimeField(auto_now_add=True)
#     client_ip = models.GenericIPAddressField()
#     #ip_address = models.GenericIPAddressField()
#     action = models.CharField(max_length=100)
#     username = models.CharField(max_length=150, default='anonymous')
#     def __str__(self):
#         return f'{self.timestamp} - {self.client_ip} - {self.action} - {self.username}'


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
    


class BullyAlgorithm:
    def __init__(self, server_id, all_servers):
        self.server_id = server_id
        self.all_servers = all_servers

    def leader_election(self):
        highest_server_id = max(self.all_servers)
        if highest_server_id == self.server_id:
            print(f"Server {self.server_id} becomes the leader.")
        else:
            print(f"Server {highest_server_id} is the leader.")

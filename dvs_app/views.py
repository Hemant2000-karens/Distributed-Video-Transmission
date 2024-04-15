from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from .models import BroadcastingInfo

# def show_broadcast(request):
#     current_time = timezone.now()
#     broadcast_info = BroadcastingInfo.objects.first()  # Fetch broadcasting info from database
#     return render(request, 'show_broadcast.html', {'current_time': current_time, 'broadcast_info': broadcast_info})


def show_broadcast(request):
    current_time = timezone.now()
    broadcast_info = BroadcastingInfo.objects.first()  # Fetch broadcasting info from database
    if broadcast_info:
        broadcast_info.viewers_count += 1  # Increment viewers count
        broadcast_info.save()
    return render(request, 'show_broadcast.html', {'current_time': current_time, 'broadcast_info': broadcast_info})

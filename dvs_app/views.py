from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.

from django.utils import timezone
from .models import BroadcastingInfo

# def show_broadcast(request):
#     current_time = timezone.now()
#     broadcast_info = BroadcastingInfo.objects.first()  # Fetch broadcasting info from database
#     return render(request, 'show_broadcast.html', {'current_time': current_time, 'broadcast_info': broadcast_info})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def show_broadcast(request):
    current_time = timezone.now()
    broadcast_info = BroadcastingInfo.objects.first()  # Fetch broadcasting info from database
    if broadcast_info:
        broadcast_info.viewers_count += 1  # Increment viewers count
        broadcast_info.save()
    return render(request, 'show_broadcast.html', {'current_time': current_time, 'broadcast_info': broadcast_info})

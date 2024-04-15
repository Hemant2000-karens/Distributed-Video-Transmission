from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.utils import timezone
from .models import BroadcastingInfo
from django.urls import reverse
# def show_broadcast(request):
#     current_time = timezone.now()
#     broadcast_info = BroadcastingInfo.objects.first()  # Fetch broadcasting info from database
#     return render(request, 'show_broadcast.html', {'current_time': current_time, 'broadcast_info': broadcast_info})
def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # Redirect to homepage if user is already logged in
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            error_message = 'Invalid username or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

@login_required  # Add this decorator to restrict access to authenticated users only
def show_broadcast(request):
    current_time = timezone.now()
    broadcast_info = BroadcastingInfo.objects.first()
    if broadcast_info:
        broadcast_info.viewers_count += 1
        broadcast_info.save()
    return render(request, 'show_broadcast.html', {'current_time': current_time, 'broadcast_info': broadcast_info})

@login_required
def home_view(request):
    return render(request, 'homepage.html')
                  

def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return HttpResponseRedirect(reverse('login'))  # Replace '/login/' with your login URL






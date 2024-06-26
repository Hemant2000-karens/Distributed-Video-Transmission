from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.utils import timezone
from .models import BroadcastingInfo
from django.urls import reverse


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import BroadcastingInfo
from .models import ApplicationLog
from .models import ClientInteractionLog
from .models import BullyAlgorithm
import threading
import multiprocessing


servers = [1, 2, 3]
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

# @login_required  # Add this decorator to restrict access to authenticated users only
# def show_broadcast(request):
#     current_time = timezone.now()
#     broadcast_info = BroadcastingInfo.objects.first()
#     if broadcast_info:
#         broadcast_info.viewers_count += 1
#         broadcast_info.save()
#     return render(request, 'show_broadcast.html', {'current_time': current_time, 'broadcast_info': broadcast_info})

@login_required
def home_view(request):
    current_time = timezone.now()
    broadcast_info = BroadcastingInfo.objects.first()
    bully_algorithm = BullyAlgorithm(server_id=request.server_id, all_servers=servers)
    bully_algorithm.leader_election()
    return render(request, 'homepage.html', {'current_time': current_time, 'broadcast_info': broadcast_info})

                  

def logout_view(request):
    logout(request)
    # Redirect to a page after logout
    return HttpResponseRedirect(reverse('login'))  # Replace '/login/' with your login URL

# views.py


# @require_POST
# def update_watch_count(request):
#     if request.user.is_authenticated:
#         if request.POST.get('action') == 'play':
#             video_id = request.POST.get('video_id')
#             try:
#                 video = Video.objects.get(pk=video_id)
#                 video.watch_count += 1
#                 video.save()
#                 return JsonResponse({'success': True})
#             except Video.DoesNotExist:
#                 return JsonResponse({'success': False, 'error': 'Video not found.'})
#         else:
#             return JsonResponse({'success': False, 'error': 'Invalid action.'})
#     else:
#         return JsonResponse({'success': False, 'error': 'Authentication required.'})


# views.py

# @require_POST
# def update_watch_count(request):
#     if request.user.is_authenticated:
#         if request.POST.get('action') == 'play':
#             video_id = request.POST.get('video-player')
#             try:
#                 broadcast_info = BroadcastingInfo.objects.get(pk=video_id)
#                 broadcast_info.viewers_count += 1
#                 broadcast_info.save()
#                 return JsonResponse({'success': True})
#             except BroadcastingInfo.DoesNotExist:
#                 return JsonResponse({'success': False, 'error': 'Broadcasting info not found.'})
#         else:
#             return JsonResponse({'success': False, 'error': 'Invalid action.'})
#     else:
#         return JsonResponse({'success': False, 'error': 'Authentication required.'})


# views.py


@require_POST
def update_watch_count(request):
    video_id = request.POST.get('video_id')
    try:
        broadcast_info = BroadcastingInfo.objects.get(video_id=video_id)
        broadcast_info.viewers_count += 1
        broadcast_info.save()
        return JsonResponse({'success': True})
    except BroadcastingInfo.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Broadcasting info not found.'})

# views.py


@login_required
def my_view(request):
    # Log application actions
    ApplicationLog.objects.create(action='User viewed a video')
    

    client_ip = request.META.get('REMOTE_ADDR')
    action = 'Performed some action'  # Update with your action
    
    # Create a new log entry
    log_entry = ClientInteractionLog.objects.create(
        client_ip=client_ip,action=action
    )
    server_id = request.session.get('server_id')
    # Return a JSON response indicating success
    return JsonResponse({'success': True, 'server_id': server_id})
    # Your view logic...


# Create a global lock object
lock = threading.Lock()

def synchronized_view(request):
    # Acquire the lock before accessing the critical section
    lock.acquire()
    try:
        # Critical section - Access shared resources here
        # For example, update a shared database record
        # Ensure that any database operations are atomic
        # Return a JSON response indicating success or failure
        return JsonResponse({'success': True})
    finally:
        # Release the lock after completing the critical section
        lock.release()


lock = multiprocessing.Lock()

def synchronized_view(request):
    # Acquire the lock before accessing the critical section
    lock.acquire()
    try:
        # Critical section - Access shared resources here
        # Ensure that any operations are thread-safe
        # Return a JSON response indicating success or failure
        return JsonResponse({'success': True})
    finally:
        # Release the lock after completing the critical section
        lock.release()
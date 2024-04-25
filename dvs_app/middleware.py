# middleware.py
import ntplib
from .models import ClientInteractionLog
from ntplib import NTPException
import time
from django.conf import settings

class ClientInteractionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture client interactions
        ip_address = request.META.get('REMOTE_ADDR')
        action = request.path_info  # Assuming path_info represents the action

        if request.user.is_authenticated:
            username = request.user.username
        else:
            username = "Anonymous" 
        ClientInteractionLog.objects.create(client_ip=ip_address, action=action, username=username)
        response = self.get_response(request)
        return response


class NTPTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.ntp_time = self.synchronize_time()
        response = self.get_response(request)
        return response

    def synchronize_time(self, max_retries=3, retry_interval=1):
        retries = 0
        while retries < max_retries:
            try:
                client = ntplib.NTPClient()
                response = client.request('in.pool.ntp.org', version=3)
                if response:
                    return response.tx_time
            except NTPException as e:
                print(f"NTP synchronization failed: {e}")
                retries += 1
                time.sleep(retry_interval)
                return time.time()
        return None 


class BullyAlgorithmMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Initialize server list
        servers = [1, 2, 3]
        request.server_id = 1  # Example server id
        response = self.get_response(request)
        return response

class LoadBalancerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Perform load balancing logic here
        # For demonstration, we'll simply alternate between two server IDs
        if 'server_id' not in request.session:
            request.session['server_id'] = 1
        else:
            request.session['server_id'] = 2 if request.session['server_id'] == 1 else 1

        # Continue processing the request
        response = self.get_response(request)
        return response
# middleware.py
import ntplib
from .models import ClientInteractionLog
from ntplib import NTPException
import time

class ClientInteractionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture client interactions
        ip_address = request.META.get('REMOTE_ADDR')
        action = request.path_info  # Assuming path_info represents the action
        ClientInteractionLog.objects.create(client_ip=ip_address, action=action)
        
        # Pass the request to the next middleware or view
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

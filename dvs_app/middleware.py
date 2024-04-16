# middleware.py
import ntplib
from .models import ClientInteractionLog

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

    def synchronize_time(self):
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3)
        return response.tx_time

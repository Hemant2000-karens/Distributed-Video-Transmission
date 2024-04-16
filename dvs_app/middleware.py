# middleware.py

from .models import ClientInteractionLog

class ClientInteractionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capture client interactions
        ip_address = request.META.get('REMOTE_ADDR')
        action = request.path_info  # Assuming path_info represents the action
        ClientInteractionLog.objects.create(ip_address=ip_address, action=action)
        
        # Pass the request to the next middleware or view
        response = self.get_response(request)
        return response

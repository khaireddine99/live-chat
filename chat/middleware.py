import logging

# Set up a logger
logger = logging.getLogger(__name__)

class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get IP address
        ip_address = request.META.get('REMOTE_ADDR')
        # Log the IP address
        logger.info(f"Visitor IP: {ip_address}")
        # Continue processing the request
        response = self.get_response(request)
        return response

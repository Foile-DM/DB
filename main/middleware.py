import socket


class SaveUserInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            request.user_ip = request.META.get('REMOTE_ADDR')
            request.pc_name = socket.gethostname()
        response = self.get_response(request)
        return response

from django.shortcuts import redirect
from django.contrib import messages

class CheckAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        
        # print(request.path)
        path = request.path.split('/')[1]
        
        if path == 'app' and not request.user.is_authenticated:
            messages.error(request, "Please login first to access this page")
            return redirect('login_view')
        else:
            response = self.get_response(request)
            return response
            

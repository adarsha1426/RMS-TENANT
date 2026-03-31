from django.http import JsonResponse

from users.models import CustomUser
from rest_framework.response import Response


class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before any request is called
        print("Before view")
        reponse = self.get_response(request)
        if reponse:
            print("After View")
        return reponse


class AuthInterceptorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def check_valid_user(self, user: CustomUser):
        if user.is_anonymous:
            return "", False, None
        return user.role, True, user

    def __call__(self, request):
        response = self.get_response(request)
        role, ok, user = self.check_valid_user(request.user)
        path: str = request.path
        if path.startswith("/api/"):
            return response
        if ok:
            if user.is_active and role == "admin" and user.is_superuser:
                return response
        response = JsonResponse(
            dict(
                message="Not Authenticated",
            ),
        )
        response.status_code = 401
        return response

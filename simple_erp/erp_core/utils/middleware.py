from django.core.exceptions import BadRequest
from django.http import HttpResponse

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from rest_framework import status


class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        print('Custom Middleware was loaded!')
        self.get_response = get_response

    def __call__(self, request):
        print('Customer Middleware was called!')
        username = request.headers.get('username', '')
        password = request.headers.get('password', '')
        if not username or not password:
            response = HttpResponse('Missing username and/or password field in header!')
            setattr(response, 'status_code', status.HTTP_200_OK)
            return response

        user = User.objects.all().filter(username=username).first()
        if not user:
            response = HttpResponse('Username does not exist!')
            setattr(response, 'status_code', status.HTTP_200_OK)
            return response

        authorized = check_password(password, user.password)
        if not authorized:
            response = HttpResponse('Password is not corrected!')
            setattr(response, 'status_code', status.HTTP_200_OK)
            return response

        return self.get_response(request)

from django.shortcuts import render
from rest_framework.viewsets import ViewSet

from account.models import User
from .serializers import LoginSerializer


class LoginViewSet(ViewSet):
    queryset = User.objects.all()
    serializers_class = LoginSerializer

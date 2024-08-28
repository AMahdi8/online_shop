from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginViewSet

rotuer = DefaultRouter()
rotuer.register('login', LoginViewSet)

urlpatterns = rotuer.urls
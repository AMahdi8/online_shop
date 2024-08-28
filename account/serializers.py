from rest_framework import serializers

from .models import User


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'password']

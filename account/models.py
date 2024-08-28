from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from .utilities import phone_number_validator


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number or not password:
            raise ValueError('The phone number and password must be set')

        phone_number_validator(phone_number)

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    username = None

    phone_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(blank=True, null=True)

    objects = UserManager()

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.phone_number

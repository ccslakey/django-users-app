from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, blank=False, unique=True, primary_key=True)
    USERNAME_FIELD = 'phone_number'
    def __str__(self):
        return self.phone_number

    def get_full_name(self):
        return self.phone_number

    def get_short_name(self):
        return self.phone_number

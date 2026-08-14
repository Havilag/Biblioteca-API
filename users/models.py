from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=9, blank=True)
    address = models.CharField(max_length=255, blank=True)
    
    
    def __str__(self):
        return self.username

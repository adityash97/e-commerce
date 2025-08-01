from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserAuth(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # avoids asking for username in createsuperuser
    email = models.EmailField(max_length=250,unique=True)
    
    def __str__(self):
        return self.email
                
    
    
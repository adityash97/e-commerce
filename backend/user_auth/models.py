from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserAuth(AbstractUser):
    email = models.EmailField(max_length=250,unique=True)
    
    def save(self,*args,**kwargs):
        if not self.username:
            basename = self.email.split('@')[0]
            counter = 1
            unique_username = basename
            while UserAuth.objects.filter(username = unique_username).exists():
                unique_username = basename + str(counter)
                counter+=1
            self.username = unique_username
        super().save(*args,**kwargs)   
    def __str__(self):
        return self.email
                
    
    
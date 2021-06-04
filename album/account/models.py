from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullName = models.CharField(max_length=128)
    follow = models.ManyToManyField(to='self', blank=True, null=True)
    webcollor = models.CharField(max_length=128, default='white')
    
    def __str__(self):
        return self.fullName + '(' + self.username + ')'
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    email = models.EmailField(('email address'), unique=True)

    def __str__(self):
        return self.email


class Shop(models.Model):

    name_shop = models.CharField(max_length=255)
    unp = models.IntegerField()
    
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)

    def __str__(self):
        return self.name_shop
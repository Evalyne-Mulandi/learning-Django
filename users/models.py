from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    STATUS = (
        ('reqular', 'reqular'),
        ('subscriber', 'subscriber'),
        ('moderator','moderator')

    )

    email = models.EmailField(max_length=254, unique= True)
    Status = models.CharField(max_length= 20 , choices= STATUS, default='reqular')
    description= models.TextField('description',max_length=600,default='', blank=True)
    
    def __str__(self):
        return self.username
    

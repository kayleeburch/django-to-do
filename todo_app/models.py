from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
    # def __str__(self):
    #     return f"ID: {self.id} Title: {self.title} Body: {self.body}"
    
class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length=255,
        unique=True,
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class Todo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField(max_length=255)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
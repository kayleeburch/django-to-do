from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField(max_length=255)
    
    # def __str__(self):
    #     return f"ID: {self.id} Title: {self.title} Body: {self.body}"
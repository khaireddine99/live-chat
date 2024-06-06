from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Message(models.Model):
    author = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.author}: {self.body[:50]}'

class Post(models.Model):
    owner = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title 
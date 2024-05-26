from django.db import models

# Create your models here.
class Message(models.Model):
    author = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'{self.author}: {self.body[:50]}'
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email  = models.EmailField()
    # Define gender choices
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    # Add the gender field
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=False)

    gay = models.BooleanField(default=True)

    def __str__(self):
        return self.username
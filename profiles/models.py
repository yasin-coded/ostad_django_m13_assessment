from django.db import models
from django.conf import settings

# Create your models here.

class Profile (models.Model):
    user= models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    bio= models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

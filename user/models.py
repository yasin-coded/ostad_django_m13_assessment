from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class UserManager (BaseUserManager):
    def create_user (self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser (self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.') 
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username=username, email=email, password=password, **extra_fields)

class User(AbstractUser):
    class Role (models.TextChoices):
        ADMIN= "ADMIN", "Admin"
        STAFF= "STAFF", "Staff"
        USER= "USER", "User"

    role= models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    REQUIRED_FIELDS=['email']
    objects= UserManager()

    def __str__ (self):
        return self.username
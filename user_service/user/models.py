# from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser  # Django core
from django.db import models                        # Django ORM

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

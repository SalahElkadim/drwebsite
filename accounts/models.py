from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = 'username'  # ← التغيير هنا
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.username
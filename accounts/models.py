from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    
    # إزالة الحقول غير الضرورية
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']
    
    def __str__(self):
        return self.email
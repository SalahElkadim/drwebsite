
from django.db import models

class ConsultationRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
    
class seminarrequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"

class Visitinglog(models.Model):
    ip_address = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    visit_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.ip_address} - {self.visit_time}"
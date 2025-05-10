
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
    ip_adress = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=2048)
    country =models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return f"{self.ip_address} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
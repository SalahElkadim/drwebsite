
from django.db import models
from django.utils import timezone


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


class Visitor(models.Model):
    ip_address = models.CharField(max_length=45)
    country = models.CharField(max_length=100, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.ip_address} - {self.country} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']

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

from django.db import models
from cloudinary.models import CloudinaryField

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان الخبر")
    paragraph = models.TextField(verbose_name="نص الخبر")
    image = CloudinaryField("صورة الخبر", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "الأخبار"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Newsen(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان الخبر")
    paragraph = models.TextField(verbose_name="نص الخبر")
    image = CloudinaryField("صورة الخبر", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "الأخبار"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

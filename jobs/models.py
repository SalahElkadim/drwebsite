
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=[('Full-Time', 'دوام كامل'), ('Part-Time', 'دوام جزئي')])
    posted_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} at {self.company_name}"


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=150)
    email = models.EmailField()
    cv = models.FileField(upload_to='cvs/')
    message = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"


class CompanyRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد المراجعة'),
        ('accepted', 'مقبول'),
        ('rejected', 'مرفوض'),
    ]
    company_name = models.CharField(max_length=200, verbose_name="اسم الشركة")
    contact_email = models.EmailField(verbose_name="البريد الإلكتروني")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="هاتف الاتصال")
    job_description = models.TextField(verbose_name="وصف الوظائف")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="حالة الطلب")
    accepted_at = models.DateTimeField(null=True, blank=True, verbose_name="تاريخ القبول")
    contract_signed = models.BooleanField(default=False, verbose_name="تم توقيع العقد")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")
    
    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = "طلب شركة"
        verbose_name_plural = "طلبات الشركات"
        ordering = ['-submitted_at']

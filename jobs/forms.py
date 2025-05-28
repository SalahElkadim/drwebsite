from django import forms
from .models import JobApplication, CompanyRequest, Job

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['applicant_name', 'email', 'cv', 'message']

class CompanyRequestForm(forms.ModelForm):
    class Meta:
        model = CompanyRequest
        fields = ['company_name', 'contact_email', 'job_description']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'description', 'location', 'job_type', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'job_type': forms.Select(choices=[('Full-Time', 'دوام كامل'), ('Part-Time', 'دوام جزئي')]),
        }
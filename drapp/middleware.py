from .models import Visitor
from django.utils import timezone
from django_user_agents.utils import get_user_agent
import os
from django.conf import settings

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # تجنب تسجيل الزيارات من قبل المشرفين
        if not request.path.startswith('/admin/'):
            ip_address = self.get_client_ip(request)
            user_agent = get_user_agent(request)
            
            # الحصول على معلومات البلد
            country = self.get_country(ip_address)
            
            Visitor.objects.create(
                ip_address=ip_address,
                country=country,
                user_agent=str(user_agent),
                referrer=request.META.get('HTTP_REFERER', ''),
                path=request.path
            )

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

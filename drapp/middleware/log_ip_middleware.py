from drapp.models import Visitinglog
from django.utils.timezone import now
from drapp.utils import get_country_from_ip


class LogIPMiddleware:
    def __init__(self, get_response):  # تصحيح: __init__ بدل _init_
        self.get_response = get_response

    def __call__(self, request):  # تصحيح: __call__ بدل _call_
        ip = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')[:200]  # تحديد طول النص
        path = request.path[:200]  # تحديد طول النص
        country = get_country_from_ip(ip)

        try:
            Visitinglog.objects.create(
                ip_address=ip,
                country=country,
                user_agent=user_agent,
                path=path,
                visit_time=now()  # إضافة وقت الزيارة
            )
        except Exception as e:
            # تسجيل الخطأ دون إيقاف التطبيق
            print(f"Failed to log visit: {e}")

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR', '')
        return ip
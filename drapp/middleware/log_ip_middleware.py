from drapp.models import Visitinglog
from django.utils.timezone import now
from drapp.utils import get_country_from_ip  


class LogIPMiddleware:
    def _init_(self, get_response):
        self.get_response = get_response

    def _call_(self, request):
        ip = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        path = request.path
        country = get_country_from_ip(ip)

        Visitinglog.objects.create(
            ip_address=ip,
            country=country,
            user_agent=user_agent,
            path=path
)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    





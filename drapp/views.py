from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import ConsultationRequest, seminarrequest, Visitor
from django.utils import timezone
from datetime import timedelta

def home (request):
    return render(request, 'drapp/home.html')

def about (request):
    return render(request, 'drapp/about.html')

def consult (request):
    return render(request, 'drapp/consultation.html')

def privacy (request):
    return render(request, 'drapp/privacy.html')

def helpcenter (request):
    return render(request, 'drapp/helpcenter.html')

def forensic (request):
    return render(request, 'drapp/forensic.html')

def marketing (request):
    return render(request, 'drapp/marketing.html')

def academic (request):
    return render(request, 'drapp/academic.html')

def seminar (request):
    return render(request, 'drapp/seminar.html')


# views.py



@csrf_exempt
def submit_consultation(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # حفظ البيانات في قاعدة البيانات
        consultation = ConsultationRequest.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            service=data.get('service'),
            message=data.get('message'),
        )

        # إرسال بريد لمقدم الخدمة
        send_mail(
            subject='استشارة جديدة من الموقع',
            message=f"""
                الاسم: {consultation.name}
                البريد: {consultation.email}
                الهاتف: {consultation.phone}
                نوع الخدمة: {consultation.service}
                التفاصيل: {consultation.message}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['M.abuzaifah@gmail.com'],  # ← غيّر البريد
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


@csrf_exempt
def submit_seminar(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # حفظ البيانات في قاعدة البيانات
        consultation = seminarrequest.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            service=data.get('service'),
            message=data.get('message'),
        )

        # إرسال بريد لمقدم الخدمة
        send_mail(
            subject='طلب حجز ندوة',
            message=f"""
                الاسم: {consultation.name}
                البريد: {consultation.email}
                الهاتف: {consultation.phone}
                نوع الجهة: {consultation.service}
                التفاصيل: {consultation.message}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['M.abuzaifah@gmail.com'],  # ← غيّر البريد
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



def visitor_stats(request):
    # الزوار اليوم
    today = timezone.now().date()
    visitors_today = Visitor.objects.filter(timestamp__date=today)
    
    # الزوار حسب البلد
    visitors_by_country = Visitor.objects.filter(timestamp__date=today).values('country').annotate(count=models.Count('id'))
    
    # عناوين IP اليوم
    ip_addresses_today = visitors_today.values_list('ip_address', flat=True).distinct()
    
    context = {
        'visitors_today': visitors_today.count(),
        'visitors_by_country': visitors_by_country,
        'ip_addresses_today': ip_addresses_today,
        'today': today,
    }
    
    return render(request, 'drapp/visitor.html', context)

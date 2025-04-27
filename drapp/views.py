from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import ConsultationRequest, seminarrequest

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
            recipient_list=['ceo@sabrconsult.com'],  # ← غيّر البريد
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
            recipient_list=['ceo@sabrconsult.com'],  # ← غيّر البريد
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

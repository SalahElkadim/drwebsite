from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import json
from .models import ConsultationRequest, seminarrequest, Visitor
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.db import models


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


def academic (request):
    return render(request, 'drapp/academic.html')

def seminar (request):
    return render(request, 'drapp/seminar.html')

def contact_view(request):
    return render(request, 'drapp/connect.html')
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


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import News
import json

def news_dashboard(request):
    """صفحة الداشبورد الرئيسية"""
    return render(request, 'drapp/dashboard.html')

def get_news_list(request):
    """جلب قائمة الأخبار"""
    news = News.objects.all()
    news_list = []
    for item in news:
        news_list.append({
            'id': item.id,
            'title': item.title,
            'paragraph': item.paragraph,
            'image': item.image.url if item.image else None,
            'created_at': item.created_at.strftime('%Y-%m-%d %H:%M')
        })
    return JsonResponse({'news': news_list})

def get_news_detail(request, pk):
    """جلب تفاصيل خبر معين"""
    news = get_object_or_404(News, pk=pk)
    return JsonResponse({
        'id': news.id,
        'title': news.title,
        'paragraph': news.paragraph,
        'image': news.image.url if news.image else None,
        'created_at': news.created_at.strftime('%Y-%m-%d %H:%M')
    })

@require_http_methods(["POST"])
def create_news(request):
    """إضافة خبر جديد"""
    try:
        title = request.POST.get('title')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')
        
        news = News.objects.create(
            title=title,
            paragraph=paragraph,
            image=image
        )
        
        return JsonResponse({
            'success': True,
            'message': 'تم إضافة الخبر بنجاح',
            'news': {
                'id': news.id,
                'title': news.title,
                'paragraph': news.paragraph,
                'image': news.image.url if news.image else None,
                'created_at': news.created_at.strftime('%Y-%m-%d %H:%M')
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

@require_http_methods(["POST"])
def update_news(request, pk):
    """تعديل خبر"""
    try:
        news = get_object_or_404(News, pk=pk)
        
        news.title = request.POST.get('title', news.title)
        news.paragraph = request.POST.get('paragraph', news.paragraph)
        
        if request.FILES.get('image'):
            news.image = request.FILES.get('image')
        
        news.save()
        
        return JsonResponse({
            'success': True,
            'message': 'تم تعديل الخبر بنجاح',
            'news': {
                'id': news.id,
                'title': news.title,
                'paragraph': news.paragraph,
                'image': news.image.url if news.image else None,
                'created_at': news.created_at.strftime('%Y-%m-%d %H:%M')
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

@require_http_methods(["POST"])
def delete_news(request, pk):
    """حذف خبر"""
    try:
        news = get_object_or_404(News, pk=pk)
        news.delete()
        return JsonResponse({'success': True, 'message': 'تم حذف الخبر بنجاح'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)
    
def news_public_page(request):
    """صفحة عرض الأخبار للمستخدمين"""
    news = News.objects.all()
    return render(request, 'drapp/public.html', {'news': news})
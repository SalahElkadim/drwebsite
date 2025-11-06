from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.db import models
import json
from django.contrib.auth.decorators import user_passes_test
from .models import ConsultationRequest, seminarrequest, News,Newsen

# ==============================
# النسخة العربية
# ==============================

def home(request):
    return render(request, 'drapp/home.html')

def about(request):
    return render(request, 'drapp/about.html')

def consult(request):
    return render(request, 'drapp/consultation.html')

def privacy(request):
    return render(request, 'drapp/privacy.html')

def helpcenter(request):
    return render(request, 'drapp/helpcenter.html')

def forensic(request):
    return render(request, 'drapp/forensic.html')

def academic(request):
    return render(request, 'drapp/academic.html')

def seminar(request):
    return render(request, 'drapp/seminar.html')

def contact_view(request):
    return render(request, 'drapp/connect.html')


# ==============================
# النسخة الإنجليزية
# ==============================

def home_en(request):
    return render(request, 'drapp/en/home.html')

def about_en(request):
    return render(request, 'drapp/en/about.html')

def consult_en(request):
    return render(request, 'drapp/en/consultation.html')

def privacy_en(request):
    return render(request, 'drapp/en/privacy.html')

def helpcenter_en(request):
    return render(request, 'drapp/en/helpcenter.html')

def forensic_en(request):
    return render(request, 'drapp/en/forensic.html')

def academic_en(request):
    return render(request, 'drapp/en/academic.html')

def seminar_en(request):
    return render(request, 'drapp/en/seminar.html')

def contact_en(request):
    return render(request, 'drapp/en/connect.html')


# ==============================
# طلبات المستخدم (العربي والإنجليزي سواسية)
# ==============================

@csrf_exempt
def submit_consultation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        consultation = ConsultationRequest.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            service=data.get('service'),
            message=data.get('message'),
        )

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
            recipient_list=['M.abuzaifah@gmail.com'],
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


@csrf_exempt
def submit_seminar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        consultation = seminarrequest.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            service=data.get('service'),
            message=data.get('message'),
        )

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
            recipient_list=['M.abuzaifah@gmail.com'],
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


# ==============================
# الأخبار
# ==============================
@user_passes_test(lambda u: u.is_superuser)
def news_dashboard(request):
    return render(request, 'drapp/dashboard.html')
def get_news_list(request):
    news = News.objects.all()
    news_list = [{
        'id': item.id,
        'title': item.title,
        'paragraph': item.paragraph,
        'image': item.image.url if item.image else None,
        'is_pinned': item.is_pinned,
        'created_at': item.created_at.strftime('%Y-%m-%d %H:%M')
    } for item in news]
    return JsonResponse({'news': news_list})

def get_news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return JsonResponse({
        'id': news.id,
        'title': news.title,
        'paragraph': news.paragraph,
        'image': news.image.url if news.image else None,
        'is_pinned': news.is_pinned,
        'created_at': news.created_at.strftime('%Y-%m-%d %H:%M')
    })

@require_http_methods(["POST"])
def create_news(request):
    try:
        title = request.POST.get('title')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')
        is_pinned = request.POST.get('is_pinned') == 'true'
        
        news = News.objects.create(
            title=title,
            paragraph=paragraph,
            image=image,
            is_pinned=is_pinned
        )
        return JsonResponse({
            'success': True,
            'message': 'تم إضافة الخبر بنجاح',
            'news': {
                'id': news.id,
                'title': news.title,
                'paragraph': news.paragraph,
                'image': news.image.url if news.image else None,
                'is_pinned': news.is_pinned,
                'created_at': news.created_at.strftime('%Y-%m-%d %H:%M')
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

@require_http_methods(["POST"])
def update_news(request, pk):
    try:
        news = get_object_or_404(News, pk=pk)
        news.title = request.POST.get('title', news.title)
        news.paragraph = request.POST.get('paragraph', news.paragraph)
        news.is_pinned = request.POST.get('is_pinned') == 'true'
        if request.FILES.get('image'):
            news.image = request.FILES.get('image')
        news.save()
        return JsonResponse({'success': True, 'message': 'تم تعديل الخبر بنجاح'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

@require_http_methods(["POST"])
def delete_news(request, pk):
    try:
        news = get_object_or_404(News, pk=pk)
        news.delete()
        return JsonResponse({'success': True, 'message': 'تم حذف الخبر بنجاح'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

def news_public_page(request):
    news = News.objects.all()
    return render(request, 'drapp/public.html', {'news': news})

def news_public_page_en(request):
    news = Newsen.objects.all()
    return render(request, 'drapp/en/public.html', {'news': news})

# ==============================
# الأخبار
# ==============================
@user_passes_test(lambda u: u.is_superuser)
def news_dashboard_en(request):
    return render(request, 'drapp/en/dashboard.html')

def get_news_list_en(request):
    news = Newsen.objects.all()
    news_list = [{
        'id': item.id,
        'title': item.title,
        'paragraph': item.paragraph,
        'image': item.image.url if item.image else None,
        'is_pinned': item.is_pinned,
        'created_at': item.created_at.strftime('%Y-%m-%d %H:%M')
    } for item in news]
    return JsonResponse({'news': news_list})

def get_news_detail_en(request, pk):
    news = get_object_or_404(Newsen, pk=pk)
    return JsonResponse({
        'id': news.id,
        'title': news.title,
        'paragraph': news.paragraph,
        'image': news.image.url if news.image else None,
        'is_pinned': news.is_pinned,
        'created_at': news.created_at.strftime('%Y-%m-%d %H:%M')
    })

@require_http_methods(["POST"])
def create_news_en(request):
    try:
        title = request.POST.get('title')
        paragraph = request.POST.get('paragraph')
        image = request.FILES.get('image')
        is_pinned = request.POST.get('is_pinned') == 'true'
        
        news = Newsen.objects.create(
            title=title,
            paragraph=paragraph,
            image=image,
            is_pinned=is_pinned
        )
        return JsonResponse({
            'success': True,
            'message': 'Article added successfully',
            'news': {
                'id': news.id,
                'title': news.title,
                'paragraph': news.paragraph,
                'image': news.image.url if news.image else None,
                'is_pinned': news.is_pinned,
                'created_at': news.created_at.strftime('%Y-%m-%d %H:%M')
            }
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

@require_http_methods(["POST"])
def update_news_en(request, pk):
    try:
        news = get_object_or_404(Newsen, pk=pk)
        news.title = request.POST.get('title', news.title)
        news.paragraph = request.POST.get('paragraph', news.paragraph)
        news.is_pinned = request.POST.get('is_pinned') == 'true'
        if request.FILES.get('image'):
            news.image = request.FILES.get('image')
        news.save()
        return JsonResponse({'success': True, 'message': 'Article updated successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)

@require_http_methods(["POST"])
def delete_news_en(request, pk):
    try:
        news = get_object_or_404(Newsen, pk=pk)
        news.delete()
        return JsonResponse({'success': True, 'message': 'Article deleted successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)
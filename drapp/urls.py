from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from .views import submit_consultation, submit_seminar

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # ==============================
    # الصفحات العربية
    # ==============================
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('consult', views.consult, name='consult'),
    path('privacy', views.privacy, name='privacy'),
    path('helpcenter', views.helpcenter, name='helpcenter'),
    path('forensic', views.forensic, name='forensic'),
    path('academic', views.academic, name='academic'),
    path('seminar', views.seminar, name='seminar'),
    path('contact/', views.contact_view, name='contact'),

    # ==============================
    # النسخ الإنجليزية
    # ==============================
    path('en/', views.home_en, name='home_en'),
    path('en/about', views.about_en, name='about_en'),
    path('en/consult', views.consult_en, name='consult_en'),
    path('en/privacy', views.privacy_en, name='privacy_en'),
    path('en/helpcenter', views.helpcenter_en, name='helpcenter_en'),
    path('en/forensic', views.forensic_en, name='forensic_en'),
    path('en/academic', views.academic_en, name='academic_en'),
    path('en/seminar', views.seminar_en, name='seminar_en'),
    path('en/contact/', views.contact_en, name='contact_en'),

    # ==============================
    # الأخبار
    # ==============================
    path('dashboard/', views.news_dashboard, name='dashboard'),
    path('api/news/', views.get_news_list, name='news_list'),
    path('api/news/<int:pk>/', views.get_news_detail, name='news_detail'),
    path('api/news/create/', views.create_news, name='news_create'),
    path('api/news/<int:pk>/update/', views.update_news, name='news_update'),
    path('api/news/<int:pk>/delete/', views.delete_news, name='news_delete'),

    # ==============================
    # الأخبار
    # ==============================
    path('en/dashboard/', views.news_dashboard_en, name='dashboard_en'),
    path('en/api/news/', views.get_news_list_en, name='news_list_en'),
    path('en/api/news/<int:pk>/', views.get_news_detail_en, name='news_detail_en'),
    path('en/api/news/create/', views.create_news_en, name='news_create'),
    path('en/api/news/<int:pk>/update/', views.update_news_en, name='news_update_en'),
    path('en/api/news/<int:pk>/delete/', views.delete_news_en, name='news_delete_en'),

    # الصفحة العامة للأخبار
    path('news_public', views.news_public_page, name='news_public'),
    path('en/news_public', views.news_public_page_en, name='news_public_en'),

    # ==============================
    # خدمات أخرى
    # ==============================
    path('submit-consultation/', submit_consultation, name='submit_consultation'),
    path('submit-seminar/', submit_seminar, name='submit_seminar'),

    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

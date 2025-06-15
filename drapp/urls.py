from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}
from .views import submit_consultation , submit_seminar

urlpatterns = [
    path('', views.home , name='home'),
    path('about', views.about , name='about'),
    path('consult', views.consult , name='consult'),
    path('privacy', views.privacy , name='privacy'),
    path('helpcenter', views.helpcenter , name='helpcenter'),
    path('forensic', views.forensic , name='forensic'),
    path('marketing', views.marketing , name='marketing'),
    path('academic', views.academic , name='academic'),
    path('seminar', views.seminar , name='seminar'),
    path('submit-consultation/', submit_consultation, name='submit_consultation'),
    path('submit-seminar/', submit_seminar, name='submit_seminar'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('visitor-stats', views.visitor_stats, name='visitor_stats'),
    path('contact/', views.contact_view, name='contact'),




]
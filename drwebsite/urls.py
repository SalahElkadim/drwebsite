
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap, BlogSitemap  # عدل حسب المسار
sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drapp.urls')),
    path('jobs/', include('jobs.urls')),
    path('accounts/', include('accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



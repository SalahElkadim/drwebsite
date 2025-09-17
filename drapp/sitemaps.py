from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import YourModel  # لو عندك موديلات للصفحات الديناميكية

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        # هنا تحط الصفحات الثابتة
        return ['home', 'about', 'consult', 'privacy', 'helpcenter', 'forensic', 'marketing', 'academic']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return YourModel.objects.all()  # لو عندك مقالات أو صفحات ديناميكية

    def lastmod(self, obj):
        return obj.updated_at  # حقل تاريخ آخر تعديل في الموديل

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        # هنا تحط الصفحات الثابتة
        return ['home', 'about', 'consult', 'privacy', 'helpcenter', 'forensic',  'academic']

    def location(self, item):
        return reverse(item)



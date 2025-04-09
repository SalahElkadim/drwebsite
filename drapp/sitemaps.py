from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return ['home', 'about', 'consult', 'privacy', 'helpcenter', 'forensic', 'marketing', 'academic',]
    
    def location(self, item):
        return reverse(item)
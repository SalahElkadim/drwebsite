from django.contrib import admin
from .models import *

admin.site.register(ConsultationRequest)
admin.site.register(seminarrequest)
admin.site.register(Visitor)

from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)

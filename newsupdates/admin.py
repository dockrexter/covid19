from django.contrib import admin
from .models import News
# Register your models here.



class NewsAdmin(admin.ModelAdmin):
    list_display=("title","slug","status","created_on")
    list_filter=("status",)
    search_fields=["title","content"]
    prepopulated_fields={"slug":("title",)}


admin.site.register(News,NewsAdmin)
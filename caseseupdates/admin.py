from django.contrib import admin
from .models import Case
# Register your models here.

class CaseAdmin(admin.ModelAdmin):
    list_display=("created_on","author")
    list_filter=("created_on",)
    search_fields=["author","created_on"]



admin.site.register(Case,CaseAdmin)
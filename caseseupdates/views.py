from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Case
# Create your views here.
def index(request):
    if request.method=='GET':
        sum_active=Case.objects.aggregate(Sum('active'))
        return render(request,"caseseupdates/case.html",{'sum':sum_active['active__sum']})
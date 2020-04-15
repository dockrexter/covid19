from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Case
# Create your views here.
def index(request):
    if request.method=='GET':
        sum_active=Case.objects.aggregate(Sum('active'))
        recovered=Case.objects.aggregate(Sum('recovered'))
     
        return render(request,"caseseupdates/case.html",{'total_active':sum_active['active__sum'],'total_recovered':recovered['recovered__sum']})

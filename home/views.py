from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Sum
from caseseupdates.models import Case

# Create your views here.
def index(request):
    if request.method=='GET':
        sum_active=Case.objects.aggregate(Sum('active'))
        recovered=Case.objects.aggregate(Sum('recovered'))
        deaths=Case.objects.aggregate(Sum('deaths'))
        confirmed=Case.objects.aggregate(Sum('confirmed'))
        quarantined=Case.objects.aggregate(Sum('quarantined'))
     
        return render(request,"home/home.html",{'total_active':sum_active['active__sum'],'total_recovered':recovered['recovered__sum'],'total_deaths':deaths['deaths__sum'],'total_confirmed':confirmed['confirmed__sum'],'total_quarantined':quarantined['quarantined__sum']})

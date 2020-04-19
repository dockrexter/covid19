from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Sum
from caseseupdates.models import Case
from django.http import JsonResponse
from blog.models import Post
from healthtips.models import Tips
from newsupdates.models import News



# Create your views here.
def index(request):
    if request.method=='GET':
        sum_active=Case.objects.aggregate(Sum('active'))
        recovered=Case.objects.aggregate(Sum('recovered'))
        deaths=Case.objects.aggregate(Sum('deaths'))
        confirmed=Case.objects.aggregate(Sum('confirmed'))
        quarantined=Case.objects.aggregate(Sum('quarantined'))
        queryset1=(Post.objects.filter(status=1).order_by('-created_on'))
        queryset2=(Tips.objects.filter(status=1).order_by('-created_on'))
        queryset3=(News.objects.filter(status=1).order_by('-created_on'))

        return render(request,"home/home.html",{'newspost':queryset3,'tipspost':queryset2,'blogpost':queryset1,'total_active':sum_active['active__sum'],'total_recovered':recovered['recovered__sum'],'total_deaths':deaths['deaths__sum'],'total_confirmed':confirmed['confirmed__sum'],'total_quarantined':quarantined['quarantined__sum']})

def get_data(request):
    dates=Case.objects.values('created_on')
    q_deaths=Case.objects.values('deaths')
    q_re=Case.objects.values('recovered')
    q_qua=Case.objects.values('quarantined')
    q_a=Case.objects.values('active')
    q_c=Case.objects.values('confirmed')
    days=[]
    deaths=[]
    prev_d=0
    quarantined=[]
    prev_q=0
    active=[]
    prev_a=0
    recovered=[]
    prev_r=0
    confirmed=[]
    prev_c=0
    for i in range(len(q_deaths)):
        deaths.append(q_deaths[i]["deaths"]+prev_d)
        # prev_d+=q_deaths[i]["deaths"]
        quarantined.append(q_qua[i]["quarantined"]+prev_q)
        # prev_q+=q_qua[i]["quarantined"]
        active.append(q_a[i]["active"]+prev_a)
        # prev_a+=q_a[i]["active"]
        recovered.append(q_re[i]["recovered"]+prev_r)
        # prev_r+=q_re[i]["recovered"]
        confirmed.append(q_c[i]["confirmed"]+prev_c)
        # prev_c+=q_c[i]["confirmed"]
    for i in dates:
        days.append(i["created_on"].date().strftime("%d-%b-%Y"))
    print(list(reversed(days)))
    data={
        "dates":list(reversed(days)),
        "deaths":list(reversed(deaths)),
        "quarantined":list(reversed(quarantined)),
        "active":list(reversed(active)),
        "recovered":list(reversed(recovered)),
        "confirmed":list(reversed(confirmed))

    }
    return JsonResponse(data)
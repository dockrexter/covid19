from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ReportCase


# Create your views here.
def index(request):
     if request.method == 'POST':
          r = ReportCase.objects.create(name=request.POST["firstname"], suspect_name=request.POST["sname"],email=request.POST["email"],contact=request.POST["phone"],address=request.POST["country"],city=request.POST["country"],longitude=request.POST["long"],latitude=request.POST["lat"])
          r.save()
          return render(request,'reportcase/reportcase.html')
     return render(request,'reportcase/reportcase.html')

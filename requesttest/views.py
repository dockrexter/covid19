from django.shortcuts import render
from django.http import HttpResponse
from .models import RequestTest
# Create your views here.
def index(request):
     if request.method == 'POST':
          r = RequestTest.objects.create(name=request.POST["firstname"], gender=request.POST["gender"],email=request.POST["email"],contact=request.POST["phone"],address=request.POST["country"],city=request.POST["country"],longitude=request.POST["long"],latitude=request.POST["lat"])
          r.save()
          return render(request,'requesttest/requesttest.html')
     return render(request,'requesttest/requesttest.html')

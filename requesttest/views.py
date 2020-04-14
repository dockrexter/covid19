from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
     if request.method == 'POST':
          return HttpResponse(request.POST.items())
          
     return render(request,'requesttest/requesttest.html')

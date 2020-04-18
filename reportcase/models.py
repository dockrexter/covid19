from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class ReportCase(models.Model):
    name=models.CharField(max_length=200,blank=False,null=False)
    suspect_name=models.CharField(max_length=200,blank=False,null=False)
    email=models.CharField(max_length=200,blank=False,null=False)
    contact=models.CharField(max_length=200,blank=False,null=False)
    address=models.CharField(blank=False,null=False,max_length=500)
    city=models.CharField(blank=False,null=False,max_length=200)
    longitude=models.DecimalField(max_digits=9, decimal_places=6)
    latitude=models.DecimalField(max_digits=9, decimal_places=6)
    date=models.DateTimeField(auto_now_add=True)


   
    class Meta:
        ordering=['-date']

    
    def __str__(self):
        return str(self.date)
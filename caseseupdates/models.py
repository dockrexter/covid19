from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Case(models.Model):
    confirmed=models.IntegerField(blank=False,null=False)
    active=models.IntegerField(blank=False,null=False)
    quarantined=models.IntegerField(blank=False,null=False)
    recovered=models.IntegerField(blank=False,null=False)
    deaths=models.IntegerField(blank=False,null=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    updated_on=models.DateTimeField(auto_now=True)
    created_on=models.DateTimeField(auto_now_add=True)
    

    
    class Meta:
        ordering=['-created_on']

    
    def __str__(self):
        return str(self.author)
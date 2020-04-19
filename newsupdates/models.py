from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS=(
    (0,"Draft"),
    (1,"Publish")
)


class News(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="newsupdates_posts")
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS,default=0)
    cover_image=models.ImageField(blank=True,null=True)
    upload_to=("covers/%Y/%m/%D/")
    class Meta:
        ordering=['-created_on']

    
    def __str__(self):
        return self.title
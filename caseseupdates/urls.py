from django.urls import path
from . import views

urlpatterns = [
    path('', views.CaseList.as_view(), name='caseseupdates')
 ]
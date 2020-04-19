from django.urls import path

from . import views

urlpatterns = [
    path('', views.NewsList.as_view(), name='newsupdates'),
    path('<slug:slug>/',views.NewsDetail.as_view(),name='NewsDetail')
]

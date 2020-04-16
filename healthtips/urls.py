from django.urls import path

from . import views

urlpatterns = [
    path('', views.TipsList.as_view(), name='healthtips'),
    path('<slug:slug>/',views.TipsDetail.as_view(),name='TipsDetail')
]

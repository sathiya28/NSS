from django.urls import path, include
from django.http import request
from django.urls import path

from nss import views


app_name = 'nss'

urlpatterns = [
    path('camp/',views.campListView.as_view()),
    path('sapling/', views.Imageuploadviewset.as_view(),name='sapling'), 
    path('awards/', views.Awarduploadviewset.as_view(),name='awards'),
    path('bdc/', views.bdcListView.as_view(),name='Blood Donation-camp'),
    path('conference/', views.seminarListView.as_view(),name='Seminar -conference'), 


]

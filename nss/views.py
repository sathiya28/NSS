from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, authentication, permissions
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from django.contrib.auth.models import User
from .models import imageupload
from .serializers import imageuploadSerializer
from django.http import JsonResponse
from . models import camp
from .serializers import campSerializer
from . models import bdcupload
from . serializers import bdcuploadSerializer
from . models import seminarupload
from . serializers import seminaruploadSerializer

from .models import awardsupload
from . serializers import awarduploadSerializer
class Imageuploadviewset(generics.ListAPIView):
    queryset = imageupload.objects.all()
   
    
    serializer_class = imageuploadSerializer

class Awarduploadviewset(generics.ListAPIView):
    queryset = awardsupload.objects.all()
   
    
    serializer_class = awarduploadSerializer

class campListView(generics.ListAPIView):
    

    queryset = camp.objects.all()
    serializer_class = campSerializer

class bdcListView(generics.ListAPIView):
    

    queryset = bdcupload.objects.all()
    serializer_class = bdcuploadSerializer

class seminarListView(generics.ListAPIView):
    

    queryset = seminarupload.objects.all()
    serializer_class = seminaruploadSerializer
    
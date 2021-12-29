from rest_framework import serializers
from . models import imageupload
from . models import awardsupload

from .models import camp
from . models import bdcupload
from . models import seminarupload

class campSerializer(serializers.ModelSerializer):
    class Meta:
        model = camp
        fields='__all__'
        
class imageuploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = imageupload
        fields = '__all__'

class awarduploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = awardsupload
        fields = '__all__'

class bdcuploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = bdcupload
        fields = '__all__'

class seminaruploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = seminarupload
        fields = '__all__'







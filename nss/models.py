from django.db import models
import os
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin

# Create your models here.


def image_file_path(instance,filename):
    ext=filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join("",filename)



# camp organised
class camp(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=60)
    youtube_link = models.URLField(max_length = 200,unique=True)
    

#sapling
class imageupload(models.Model):
    title = models.CharField(max_length=50)
    sapling = models.CharField(max_length=60)
    description = models.CharField(max_length=160)
    start_date = models.DateField(blank=True, null=True) 
    end_date=models.DateField(blank=True, null=True) 
    images = models.ImageField(null=True,upload_to=image_file_path)
    # file = models.FileField(null=True,upload_to=image_file_path)

# awards and achievements
class awardsupload(models.Model):
    title = models.CharField(max_length=250)
    
    images = models.ImageField(null=True,upload_to=image_file_path)
    # file = models.FileField(null=True,upload_to=image_file_path)

#blood donation camp
class bdcupload(models.Model):   
    date = models.DateField(blank=True, null=True) 
    description = models.CharField(max_length=160) 
    units= models.CharField(max_length=60)
    images = models.ImageField(null=True,upload_to=image_file_path)

#seminar conference
class seminarupload(models.Model):   
    date = models.DateField(blank=True, null=True) 
    description = models.CharField(max_length=360) 
    images = models.ImageField(null=True,upload_to=image_file_path)








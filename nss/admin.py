from django.contrib import admin
from django.db import models

from . models import camp
from nss import models

admin.site.register(camp)
admin.site.register(models.imageupload) 
admin.site.register(models.awardsupload)
admin.site.register(models.bdcupload)
admin.site.register(models.seminarupload)
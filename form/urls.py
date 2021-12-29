
from django.contrib import admin
from django.conf.urls import url, include
# from nss.views import campListView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    url('admin/', admin.site.urls),
    url('camp/',include('nss.urls')),
    url('sapling/',include('nss.urls')),
    url('awards/',include('nss.urls')),
    url('bdc/',include('nss.urls')),
    url('seminar/',include('nss.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


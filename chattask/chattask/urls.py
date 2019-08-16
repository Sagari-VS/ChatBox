# chattask/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', include('chatapp.urls')),
    path('admin/', admin.site.urls),
]

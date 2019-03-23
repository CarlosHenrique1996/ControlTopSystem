# coding=utf-8
from django.contrib import admin
from django.urls import path, include

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('contas/', include('accounts.urls', namespace='accounts')),
]

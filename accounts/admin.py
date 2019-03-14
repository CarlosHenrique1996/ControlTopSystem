# coding=utf-8
from django.contrib import admin

from accounts.models import UserOffice, Salesman

admin.site.register(UserOffice)
admin.site.register(Salesman)
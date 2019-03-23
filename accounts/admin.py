# coding=utf-8
from django.contrib import admin

from accounts.models import Salesman

class SalesmanAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'individual_registration']

admin.site.register(Salesman, SalesmanAdmin)
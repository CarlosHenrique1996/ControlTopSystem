# coding=utf-8

from django.contrib import admin
from sales.models import Sales, SalesItem, Bag

admin.site.register(Sales)
admin.site.register(SalesItem)
admin.site.register(Bag)
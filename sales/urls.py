# coding=utf-8

from django.urls import path

from sales.views import sales_view, sales_list, create_bag_mobile, bag_list

app_name = 'sales'
urlpatterns = [
   path('caixa/', sales_view, name='sales_view'),
   path('vendas/', sales_list, name='sales_list'),
   path('criar-sacola/', create_bag_mobile, name='create_bag_mobile'),
   path('sacola/', bag_list, name='bag_list'),
]

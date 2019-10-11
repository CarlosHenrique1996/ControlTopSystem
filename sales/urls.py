# coding=utf-8

from django.urls import path

from sales.views import (
   sales_view, sales_list, create_bag_product, delete_bag_item, create_sale_view, sales_confirm
    )

app_name = 'sales'
urlpatterns = [
   path('caixa/', sales_view, name='sales_view'),
   path('vendas/', sales_list, name='sales_list'),
   path('adicionar-produto-caixa/', create_bag_product, name='create_bag_product'),
   path('excluir-produto-caixa/<int:pk>/', delete_bag_item, name='delete_bag_item'),
   path('criar-venda/', create_sale_view, name='create_sale_view'),
   path('confirmar-venda/<int:pk>', sales_confirm, name='sales_confirm'),
   
]

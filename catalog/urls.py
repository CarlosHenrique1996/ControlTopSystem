# coding=utf-8

from django.urls import path

from catalog.views import (
   create_product, save_product, list_product
   )


app_name = 'catalog'
urlpatterns = [
   path('cadastrar-produto/', create_product, name='create_product'),
   path('salvar-product/', save_product, name='save_product'),
   path('lista-de-produtos/', list_product, name='list_product'),
]

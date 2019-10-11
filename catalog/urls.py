# coding=utf-8

from django.urls import path

from catalog.views import (
   create_product, save_product, list_product,update_product,delete_product, update_product_save
   )


app_name = 'catalog'
urlpatterns = [
   path('cadastrar-produto/', create_product, name='create_product'),
   path('salvar-product/', save_product, name='save_product'),
   path('lista-de-produtos/', list_product, name='list_product'),
   path('editar-produto/<int:pk>', update_product, name='update_product'),
   path('salvar-alteracao-produto/', update_product_save, name='update_product_save'),
   path('apagar-produto/<int:pk>', delete_product, name='delete_product'),
]

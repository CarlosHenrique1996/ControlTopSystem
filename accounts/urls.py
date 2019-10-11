# coding=utf-8

from django.urls import path

from accounts.views import (
    create_salesman, save_salesman, list_salesman,update_salesman, update_salesman_save,delete_salesman
    )

app_name = 'accounts'
urlpatterns = [
    path('vendedores/', list_salesman, name='list_salesman'),
    path('cadastrar-vendedor/', create_salesman, name='create_salesman'),
    path('salvar-vendedor/', save_salesman, name='save_salesman'),
    path('alterar-vendedor/<int:pk>', update_salesman, name='update_salesman'),
    path('salvar-alteracao-vendedor/', update_salesman_save, name='update_salesman_save'),
    path('apagar-vendedor/<int:pk>', delete_salesman, name='delete_salesman'),
]
# coding=utf-8

from django.urls import path

from accounts.views import (
    create_salesman, save_salesman, list_salesman,
    )

app_name = 'accounts'
urlpatterns = [
    path('vendedores/', list_salesman, name='list_salesman'),
    path('cadastrar-vendedor/', create_salesman, name='create_salesman'),
    path('salvar-vendedor/', save_salesman, name='save_salesman'),
]
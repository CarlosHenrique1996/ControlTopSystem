# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from sales.models import Sales


class SalesItem(models.Model):

    salesman = models.ForeignKey('accounts.Salesman', verbose_name='Vendedor', on_delete=models.CASCADE, null=True)
    sales = models.ForeignKey('sales.Sales', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1) 
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Item da Venda'
        verbose_name_plural = 'Itens da Venda'

    def __str__(self):
        return "Pedido: {} - Produto: {} - Total: R$ {}".format(self.sales, self.product, (self.price * self.quantity))
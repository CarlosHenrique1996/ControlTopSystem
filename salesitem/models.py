# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from accounts.models import Salesman
from sales.models import Sales


class SalesItem(models.Model):

    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1) 
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    sales = models.ForeignKey('sales.Sales', on_delete=models.CASCADE, null=True, blank=True)
    salesman = models.ForeignKey('accounts.Salesman', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Item da Venda'
        verbose_name_plural = 'Itens da Venda'

    def __str__(self):
        return "".format(self.product * self.quantity)
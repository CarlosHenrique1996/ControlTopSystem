# coding=utf-8

import re
from django.conf import settings

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser

class Bag(models.Model):

    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='Produto')
    quantity = models.PositiveIntegerField('Quantidade', default=1) 

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Sacola'
        verbose_name_plural = 'Sacolas'

    def __str__(self):
        return "Produto: {} - Quantidade: {} - Total: R$ {}".format(self.product, self.quantity, (self.product.price * self.quantity))

class Sales(models.Model):
    
    PAYMENT_CHOICES = (
        ('cartao', 'Cartão de Crédito'),
        ('debito', 'Cartão de Débito'),
        ('dinheiro', 'Dinheiro'),
    )

    salesman = models.ForeignKey('accounts.Salesman', verbose_name='Vendedor', on_delete=models.CASCADE, null=True)
    payment = models.CharField('Forma de Pagamento', choices=PAYMENT_CHOICES, default='dinheiro', max_length=100)
    invoice = models.BooleanField('Nota Fiscal', default=False)
    
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return "{}".format(self.pk)

class SalesItem(models.Model):

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
# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser
from accounts.models import Salesman


class Sales(models.Model):
    
    total = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    payment = models.CharField('Forma de Pagamento', max_length=100)
    invoice = models.BooleanField('Nota Fiscal', default=False)
    salesman = models.ForeignKey('accounts.Salesman', related_name="Vendedor", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return self.total
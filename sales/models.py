# coding=utf-8

import re
from django.conf import settings

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser


class Sales(models.Model):
    
    salesman = models.ForeignKey('accounts.Salesman', verbose_name='Vendedor', on_delete=models.CASCADE, null=True)
    payment = models.CharField('Forma de Pagamento', max_length=100)
    invoice = models.BooleanField('Nota Fiscal', default=False)
    
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return "{}".format(self.pk)
# coding=utf-8

import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser


class Salesman(models.Model):

    name = models.CharField('Celular', max_length=15, default='', blank=True)
    sales_total = models.IntegerField('Total de Vendas', default=0)
    
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.sales_total

class UserOffice(AbstractUser):

    phone = models.CharField('Celular', max_length=15, default='', blank=True)
    individual_registration = models.CharField('CPF', max_length=14, blank=True)   
    zipcode = models.CharField('Cep', max_length=10, null=True, blank=True)
    address = models.CharField('Rua', max_length=100, null=True, blank=True)
    neighborhood = models.CharField('Bairro', max_length=30, null=True, blank=True)
    city = models.CharField('Cidade', max_length=30, null=True, blank=True)
    state = models.CharField('UF', max_length=2, null=True, blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username
    
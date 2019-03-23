# coding=utf-8

from django.db import models
from django.core import validators


class Salesman(models.Model):

    name = models.CharField('Nome', max_length=15, default='', blank=True)
    phone = models.CharField('Celular', max_length=15, default='', blank=True)
    individual_registration = models.CharField('CPF', max_length=14, blank=True)   
    zipcode = models.CharField('Cep', max_length=10, null=True, blank=True)
    address = models.CharField('Rua', max_length=100, null=True, blank=True)
    neighborhood = models.CharField('Bairro', max_length=30, null=True, blank=True)
    city = models.CharField('Cidade', max_length=30, null=True, blank=True)
    state = models.CharField('UF', max_length=2, null=True, blank=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'

    def __str__(self):
        return self.name
    
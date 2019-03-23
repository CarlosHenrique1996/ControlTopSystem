# coding=utf-8

from django.db import models

class Product(models.Model):
    
    CATEGORY_CHOICES = (
        ('computador', 'Computador'),
        ('celular', 'Celular'),
        ('acessorios', 'Acessórios'),
        ('outros', 'Outros')
    )
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=3, max_digits=8)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    warranty = models.CharField('Garantia', max_length=2)
    category = models.CharField('Categoria', choices=CATEGORY_CHOICES, default='outros', max_length=15)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        
    def __str__(self):
        return "{}".format(self.name)
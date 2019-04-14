# coding=utf-8

import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.db import models
from django.core import serializers

from sales.models import Sales, SalesItem, Bag
from catalog.models import Product
from accounts.models import Salesman

def sales_view(request):
    search_mobile = request.GET.get('search_mobile', '')
    list_mobile = None

    search_laptop = request.GET.get('search_laptop', '')
    list_laptop = None

    search_acessories = request.GET.get('search_acessories', '')
    list_acessories = None

    search_others = request.GET.get('search_others', '')
    list_others = None

    if search_mobile:
        list_mobile = Product.objects.filter(category='celular').filter(models.Q(name__icontains=search_mobile))

    if search_laptop:
        list_laptop = Product.objects.filter(category='computador').filter(models.Q(name__icontains=search_laptop))

    if search_acessories:
        list_acessories = Product.objects.filter(category='acessorios').filter(models.Q(name__icontains=search_acessories))

    if search_others:
        list_others = Product.objects.filter(category='outros').filter(models.Q(name__icontains=search_others))

    return render(request, 'sales/sales_view.html', context={
        'salesmen': Salesman.objects.all(),
        'search_mobile': search_mobile,
        'list_mobile': list_mobile,

        'search_laptop': search_laptop,
        'list_laptop': list_laptop,

        'search_acessories': search_acessories,
        'list_acessories': list_acessories,

        'search_others': search_others,
        'list_others': list_others,
    })

def sales_list(request):
    sales_list = Sales.objects.all()
    return render(request, 'sales/sales_list.html', context={
        'sales_list': sales_list,
    })

@csrf_exempt
def create_bag_mobile(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        product_pk = data.get('mobile_pk')
        quantity = data.get('quantity')    

        product = Product.objects.get(pk=product_pk)
        try:
            bag = Bag()
            bag.product = product
            bag.quantity = int(quantity)
            bag.save()
            return JsonResponse({ 'status': 202, 'message': 'Item criado na sacola.' })
        except:
            return JsonResponse({ 'status': 502, 'message': 'Erro ao criar o item na sacola.' })

def bag_list(request):
    bag_list = Bag.objects.all()
    salesmen = Salesman.objects.all()
    return render(request, 'bag/bag_list.html', context={
        'bag_list': bag_list,
        'salesmen': salesmen
    })
# coding=utf-8

import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.db import models
from django.core import serializers

from sales.models import Sales, SalesItem, Bag
from catalog.models import Product
from accounts.models import Salesman

from sales.checkout import Checkout

checkout = Checkout()

def sales_view(request):
    q = request.GET.get('q', '')
    products = None
    if q:
        products = Product.objects.filter(category__in=['celular', 'computador', 'acessorios', 'outros']).filter(models.Q(name__icontains=q))

    bag_list = Bag.objects.all()

    return render(request, 'sales/sales_view.html', context={
        'q': q,
        'salesmen': Salesman.objects.all(),
        'bag_list': bag_list,
        'products': products,
    })

def sales_list(request):
    sales_list = Sales.objects.all()
    return render(request, 'sales/sales_list.html', context={'sales_list': sales_list})

@csrf_exempt
def create_bag_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bag = Bag()
        bag.product = Product.objects.get(pk=data.get('product_pk'))
        bag.quantity = int(data.get('quantity_product'))
        bag.save()
        return redirect('sales:sales_view')

def delete_bag_item(request, pk):
    Bag.objects.filter(pk=pk).delete()
    return redirect('sales:sales_view')

def sales_confirm(request,pk):
    sales = Sales.objects.get(pk=pk)    
    salesitem = SalesItem.objects.filter(sales__pk=pk) 
    
    return render(request, 'sales/sales_confirm.html', context={
        'sales':sales,
        'salesitem':salesitem,
    })

@csrf_exempt
def create_sale_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        salesman_pk = data.get('salesman')
        payment = data.get('payment')
        bag = Bag.objects.all()
        sale = checkout.create_sale(salesman_pk, payment)
        if sale['status'] == 202:
            for i in range(0, bag.count()):
                sale_item = checkout.create_sale_item(sale['sale_pk'], bag[i].product, bag[i].quantity)
                if sale_item['status'] == 202:
                    pass
                else:
                    return HttpResponse('erro ao criar o item da venda.')
        else:
            return HttpResponse('erro ao criar a venda')
        if sale['status'] == 202 and sale_item['status'] == 202:
            bag.delete()
            return JsonResponse({'status': 202, 'url': 'teste'})
        else:
            return HttpResponse('erro ao realizar a venda.')
        return JsonResponse({ 'data': data })

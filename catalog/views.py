import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers

from catalog.models import Product 

def list_product(request):
    list_product = Product.objects.all()
    return render(request, 'catalog/list_product.html', context={
        'list_product': list_product,
    })

def create_product(request):
    return render(request, 'catalog/create_product.html', context={})


@csrf_exempt    
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalog/update_product.html',context={
        'product':product
    })
@csrf_exempt
def update_product_save(request):
    if request.method == 'POST':
        data = request.POST

        product_pk = data.get('product_pk')
        name = data.get ('name')
        description = data.get('description')
        price = data.get('price')
        quantity = data.get('quantity')
        warranty = data.get('warranty')
        category_select = data.get('category_select')

        product = Product.objects.get(pk=product_pk)
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity
        product.warranty = warranty
        product.category_select = category_select
        product.save()
    
        return redirect(reserve('catalog:list_product'))
    

def delete_product(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('catalog:list_product')



@csrf_exempt
def save_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        if ',' in price:
            price = price.replace(',', '.')
        quantity = data.get('quantity')
        warranty = data.get('warranty')
        category = data.get('category')

        product = Product()

        product.name = name
        product.description = description
        product.price = price
        product.quantity = int(quantity)
        product.warranty = int(warranty)
        product.category = category

        product.save()

        return JsonResponse({
            'status': 202,
            'url':reverse('catalog:create_product'),
        })


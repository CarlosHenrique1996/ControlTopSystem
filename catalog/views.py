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
        'product': list_product,
    })

def create_product(request):
    return render(request, 'catalog/create_product.html', context={})

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


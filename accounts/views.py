import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers

from accounts.models import Salesman 

def list_salesman(request):
    salesmen = Salesman.objects.all()
    return render(request, 'accounts/list_salesman.html', context={
        'salesmen': salesmen,
    })

def create_salesman(request):
    return render(request, 'accounts/create_salesman.html')

@csrf_exempt
def save_salesman(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        phone = data.get('phone')
        individual_registration = data.get('individual_registration')
        if Salesman.objects.filter(individual_registration=individual_registration):
            return JsonResponse({ 'status': 502, 'message': 'Já existe um vendedor com esse cpf.', 'url': reverse('accounts:create_salesman') })
        else:
            salesman = Salesman()
            salesman.name = name
            salesman.phone = phone
            salesman.individual_registration = individual_registration
            salesman.save()
            return redirect(reverse('accounts:list_salesman'))

def update_salesman(request, pk):
    salesman = Salesman.objects.get(pk=pk)
    return render(request, 'accounts/update_salesman.html', context={
        'salesman': salesman
    })

@csrf_exempt
def update_salesman_save(request):
    if request.method == 'POST':
        data = request.POST

        salesman_pk = data.get('salesman_pk')
        name = data.get('name')
        phone = data.get('phone')
        individual_registration = data.get('individual_registration')

        salesman = Salesman.objects.get(pk=salesman_pk)
        salesman.name = name
        salesman.phone = phone
        salesman.individual_registration = individual_registration
        salesman.save()

        return redirect(reverse('accounts:list_salesman'))


def delete_salesman(request, pk):
    Salesman.objects.filter(pk=pk).delete()
    return redirect('accounts:list_salesman')
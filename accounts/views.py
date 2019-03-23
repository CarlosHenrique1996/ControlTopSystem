import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

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
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        individual_registration = data.get('individual_registration')
        try:
            salesman = Salesman.objects.all()
            if Salesman.objects.filter(individual_registration=individual_registration):
                return JsonResponse({ 'status': 502, 'message': 'Já existe um vendedor com esse cpf.', 'url': reverse('accounts:create_salesman') })
            else:
                salesman = Salesman()
                salesman.name = name
                salesman.phone = phone
                salesman.individual_registration = individual_registration
                salesman.save()

            return JsonResponse({ 'status': 202, 'message': 'Usuário cadastrado.', 'url': reverse('accounts:create_salesman') })
        except:
            return JsonResponse({ 'status': 502, 'message': 'Erro ao cadastrar!', 'url': reverse('accounts:create_salesman') })
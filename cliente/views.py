from django.shortcuts import render
from django.http import HttpResponse
from cliente.models import Cliente

def home(request):
	return HttpResponse('Hello World!')


def cliente(request):
	data = {}
	data['lista_clientes'] = Cliente.objects.all()
	data['djangomoc'] = 'DjangoMOC - Curso presencial de Python e Django' 
	return render(request, 'clientes.html', data)

def cliente_update(request, pk):
	return HttpResponse('Cliente '+ str(pk))

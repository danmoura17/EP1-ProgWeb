from django.shortcuts import render
from django.http import HttpResponse
from cliente.models import Cliente
from django.shortcuts import get_object_or_404

def home(request):
	return HttpResponse('Hello World!')


def cliente(request):
	data = {}
	data['lista_clientes'] = Cliente.objects.all()
	data['djangomoc'] = 'DjangoMOC - Curso presencial de Python e Django' 
	return render(request, 'clientes.html', data)

def cliente_update(request, pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	return render(request,'cliente_detalhe.html',{'object':cliente})

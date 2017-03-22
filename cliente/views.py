from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('Hello World!')


def cliente(request):
	data = {}
	data['djangomoc'] = 'DjangoMOC - Curso presencial de Python e Django' 
	return render(request, 'clientes.html', data)

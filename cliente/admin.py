from django.contrib import admin
from cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
	model = Cliente 
	date_hierarchy = 'data_nascimento'
	list_display = ('nome', 'data_nascimento', 'salario', 'email', 'filhos')
	list_filter = ('nome', 'data_nascimento', 'salario', 'email', 'filhos')
admin.site.register(Cliente, ClienteAdmin)
# Register your models here.

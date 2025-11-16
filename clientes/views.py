from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente

# Home permanece igual
def home(request):
    return render(request, 'home.html')

# Cadastro: cria e redireciona para lista
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')

        # Validação mínima (opcional)
        if not nome or not telefone:
            # Volta pro formulário com mensagem simples (poderia usar messages)
            return render(request, 'cadastro.html', {'erro': 'Preencha nome e telefone.'})

        Cliente.objects.create(nome=nome, telefone=telefone)

        # Redireciona para a lista (usando path simples '/lista/')
        return redirect('/lista/')

# Lista: mostra todos
def lista(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'lista.html', context)

# Editar cliente: GET mostra formulário, POST atualiza
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'GET':
        return render(request, 'editar.html', {'cliente': cliente})

    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')

        if not nome or not telefone:
            return render(request, 'editar.html', {'cliente': cliente, 'erro': 'Preencha nome e telefone.'})

        cliente.nome = nome
        cliente.telefone = telefone
        cliente.save()
        return redirect('/lista/')

# Excluir cliente: suporta somente POST (mais seguro)
def excluir_cliente(request, pk):
    if request.method != 'POST':
        # opcional: pode retornar 405, mas redirecionamos à lista
        return redirect('/lista/')

    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('/lista/')

        

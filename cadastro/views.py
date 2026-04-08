# cadastro\views.py

from django.shortcuts import render

from cadastro.models import Pessoa

def index(request):

    # Recebe todas as "Pessoa" do banco de dados
    pessoas = Pessoa.objects.all()

    contexto = {
        # Passa todas as "Pessoa" para o template
        'pessoas': pessoas,
        'dono': 'Joca da Silva',
    }
    return render(request, 'cadastro/index.html', contexto)

def contato(request):
    contexto = {
        'dono': 'Joca da Silva',
    }
    return render(request, 'cadastro/contato.html', contexto)

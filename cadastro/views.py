# cadastro\views.py

from django.shortcuts import render

def index(request):
    contexto = {
        'nome': 'Joca',
        'idade': 30,
        'frutas': ['Maçã', 'Banana', 'Laranja', 'Uva'],
        'dono': 'Joca da Silva',
    }
    return render(request, 'cadastro/index.html', contexto)

def contato(request):
    contexto = {
        'dono': 'Joca da Silva',
    }
    return render(request, 'cadastro/contato.html', contexto)

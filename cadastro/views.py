# cadastro\views.py

from django.shortcuts import redirect, render

from cadastro.forms import PessoaForm
from cadastro.models import Pessoa


def index(request):

    # Recebe todas as "Pessoa" do banco de dados
    # pessoas = Pessoa.objects.all()

    # Recebe todas as "Pessoa" do banco na oredem alfabética do "nome"
    pessoas = Pessoa.objects.order_by('nome')
    total = Pessoa.objects.count()

    contexto = {
        # Passa todas as "Pessoa" para o template
        'pessoas': pessoas,
        'total': total,
    }
    return render(request, 'cadastro/index.html', contexto)


def contato(request):
    return render(request, 'cadastro/contato.html')

# Processa o formulário de cadastro de pessoas
def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()
        contexto = {
            'form': form,
        }
    return render(request, 'cadastro/adicionar.html', contexto)

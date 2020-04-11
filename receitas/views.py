from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from receitas.models import Receita


# Create your views here.
def index(request):
    receitas = Receita.objects.all()
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', context=dados)


def receitas(request,receita_id):
    context = {
        'img': 'hamburger.png'
    }
    return render(request, 'receita.html', context={'receita': get_object_or_404(Receita,pk=receita_id)})

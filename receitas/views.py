from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {
        'img': 'pizza.png'
    }
    return render(request, "receitas/templates/index.html", context=context)


def receitas(request):
    context = {
        'img': 'hamburger.png'
    }
    return render(request, 'receita.html', context=context)

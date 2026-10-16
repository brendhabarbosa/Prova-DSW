from django.shortcuts import render
from jogos.models import Equipe, Modalidade
# Create your views here.

def index(request):
    equipes = Equipe.objects.all()
    modalidade = Modalidade.objects.all()
    contexto = {
        'equipes': equipes,
        'modalidade': modalidade,
    }
    return render(request, 'jogos/index.html', contexto)

def equipe(request, id):
    equipe = get_object_or_404(Equipe, id=id)
    return render(request, 'jogos/equipe.html', {'equipe': equipe})

def modalidade(request, id):
    modalidade = get_object_or_404(Modalidade, id=id)
    return render(request, 'jogos/modalidade.html', {'modalidade': modalidade})

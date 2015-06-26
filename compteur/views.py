from django.shortcuts import render
from compteur.models import Jeu

def index(request):
    jeux = Jeu.objects.all()
    return render(request, 'index.html', {
        'jeux': jeux,
    })

def jeu_detail(request, slug):
    jeu = Jeu.objects.get(slug=slug)
    return render(request, 'jeux/jeu_detail.html', {
        'jeu': jeu,
    })
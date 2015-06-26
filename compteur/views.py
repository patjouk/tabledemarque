from django.shortcuts import render
from compteur.models import Jeu

def index(request):
    jeux = Jeu.objects.all()
    return render(request, 'index.html', {
        'jeux': jeux,
    })
from django.contrib import admin
from compteur.models import Jeu

class JeuAdmin(admin.ModelAdmin):
    model = Jeu
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Jeu, JeuAdmin)
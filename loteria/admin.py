from django.contrib import admin

# Register your models here.

from . models import Aposta, Jogos, Sorteio, Numero_sorteado, Numero_apostados


class sorteioAdmin(admin.ModelAdmin):
    list_display = ('id', 'jogo', 'data_sorteio', 'created', 'modified')

class numeroSorteadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sorteio', 'numero', 'created', 'modified')
    list_filter = ('sorteio', 'created',)

class numeroApostadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'jogo', 'numero', 'created', 'modified')
    list_filter = ('sorteio', 'created',)

admin.site.register(Jogos)
admin.site.register(Sorteio, sorteioAdmin)
admin.site.register(Numero_sorteado, numeroSorteadoAdmin)
admin.site.register(Numero_apostados)
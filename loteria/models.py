from email.policy import default
from django.db import models

class Base(models.Model):
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    
class Jogos(Base):
    nome = models.CharField(max_length=255)
    primeiro_numero = models.IntegerField()
    ultimo_numero = models.IntegerField() 
    qt_n_sorteado = models.IntegerField()   
    
    def __str__(self):
        return self.nome
    
class Aposta(Base):
    jogo = models.ForeignKey(Jogos, on_delete=models.CASCADE, verbose_name="jogos")
    
    
class Sorteio(Base):
    jogo = models.ForeignKey(Jogos, on_delete=models.CASCADE, verbose_name="jogos")
    data_sorteio = models.DateField(default='2022-11-02')
    
    def __str__(self):
        return self.jogo.nome
    
class Numero_sorteado(Base):
    sorteio = models.ForeignKey(Sorteio, on_delete=models.CASCADE, verbose_name="sorteio")
    numero = models.IntegerField()
    
    def __str__(self):
        return self.sorteio.jogo.nome
    
    
class Numero_apostados(Base):
    jogo = models.ForeignKey(Jogos, on_delete=models.CASCADE, verbose_name="jogo")
    numero = models.IntegerField()
    
    def __str__(self):
        return self.jogo.nome
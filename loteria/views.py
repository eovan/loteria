from datetime import datetime
from math import dist
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
import asyncio
from random import sample
from loteria.models import Jogos, Numero_apostados, Numero_sorteado, Sorteio
from django.contrib.auth import authenticate, login, logout


import schedule
import time

#def login(request):
    #return render(request, 'login.html',{})

def sorteioAleatorio():
    data_atual = datetime.now()
    hora_atual = data_atual.hour
    
    if hora_atual >= 20:
        jogos = Jogos.objects.all()
        
        for jogo in jogos:
            sorteio_jogos = Sorteio.objects.filter(jogo=jogo.id).filter(data_sorteio = data_atual).count()
         
            if sorteio_jogos == 0:
                primeiro_numero = jogo.primeiro_numero
                ultimo_numero = jogo.ultimo_numero + 1
                total = jogo.qt_n_sorteado
                
                #sorteados[jogo.nome] = sample(range(primeiro_numero, ultimo_numero), total)
                numeros_sorteados = sample(range(primeiro_numero, ultimo_numero), total)
           
                sorteio = Sorteio.objects.create(jogo=jogo)
            
                try: 
                    for i in numeros_sorteados:
                        Numero_sorteado.objects.create(sorteio=sorteio, numero=i)
                 
                except:
                    Sorteio.objects.filter(id=sorteio.id).delete()
    return True


def numeros(primeiro, ultimo):
    numeros = []
    
    for i in range(primeiro, (ultimo + 1)):
        if i < 10:
            valor = str("%d%d" % (0 , i))
            numeros.append(valor)
        else:
            numeros.append(str(i))  
    
    return numeros
def home(request):
    data_atual = datetime.today()
    dia_atual = data_atual.day
    sorteioAleatorio()
    numeros = get_mumeros_sorteados() 
    print(data_atual)
    sorteio = Sorteio.objects.filter(data_sorteio = data_atual)
  
    sorteio = dict()
    return render(request, 'home.html',{'sorteio':sorteio, 'numeros': numeros})

def dashboard(request):
    
    
    jogos = Jogos.objects.all()
    #sorteio = dict()
    #for x in jogos:      
        #sorteio[x.nome] = sorteioAleatorio(0,60,6)
    sorteioAleatorio()
    
    numeros = get_mumeros_sorteados()    
    #sorteio = sorteioAleatorio(0,60,6)
    
    return render(request, 'index.html',{'numeros':numeros, 'jogos': jogos})

def get_mumeros_sorteados():
    
    data_atual = datetime.now()
    
    sorteios = Sorteio.objects.all().order_by('data_sorteio', '-id')
    
    
    sorteio_jogo = {'data': []}
    jogos = Jogos.objects.all()
    
    s = Numero_sorteado.objects.select_related('sorteio').filter().order_by('-id')
    
    '''for i in s:
        if i.sorteio.id not in sorteio_jogo: 
            sorteio_jogo['data'].append(i.sorteio.id) 
            sorteio_jogo[i.sorteio.id].append({'sorteio': i.sorteio.jogo.nome})
            sorteio_jogo[i.sorteio.id].append({'data': i.sorteio.data_sorteio})
            #sorteio_jogo[i.sorteio.id].append({'numero': [i.numero]})
            
        #sorteio_jogo[i.sorteio.id].append(i.numero)
        '''
    '''for p in sorteio_jogo:
        for n in sorteio_jogo[p]:
            print(n.data)'''

        
        
        
        

    f'''or s in sorteios:
        try: 
            sorteio_jogo[s.jogo.nome] = Numero_sorteado.objects.select_related('Sorteio')
            print(sorteio_jogo )
        except:
            sorteio_jogo[s.jogo.nome] = []
    for n in sorteio_jogo:
        
        print('sorteio',n)'''
    '''numeros = Numero_sorteado.objects.filter(sorteio=sorteio.jogo.id)
    
    for x in numeros:
        print(x.sorteio)
    for x in numeros:
        print(x.sorteio)'''
        
    return s


def permitirApostas():
    data_atual = data_atual = datetime.now()
    hora_atual = data_atual.hour
    
    if hora_atual >= 22 or hora_atual <=18:
        return True
    
    else:
        return False
    
        
def apostasLoteria(request, id):
    jogo = Jogos.objects.get(pk=id)
    dados = dict()
    if request.method == 'POST':
        if permitirApostas():  
            data = request.POST
            print('data', data.items())

            #print(sorteio.jogo)
            x = 0
            print(data)
          
            for i in data:
                if x == 0: 
                    x = 1
                else:
                    Numero_apostados.objects.create(jogo=jogo, numero=int(data[i]) )
                    
                
            return redirect(dashboard)
        
            
            dados['msg'] =  'Ocorreu um erro, tenta novamente!'
                
            
        else:
            dados['msg'] =  'Fora do horário de apostas (22h às 18h)'

    numero = numeros(jogo.primeiro_numero, jogo.ultimo_numero)
    total  = []
    for x in range(jogo.qt_n_sorteado):
        total.append(x)
    dados['numeros'] = numero
    dados['total'] = total
    dados['minimo'] = jogo.primeiro_numero
    dados['maximo'] = jogo.ultimo_numero
    dados['jogo'] = jogo
       
    return render(request, 'loteria.html',dados)
   





def aut_user(request):
    if request.method == 'POST':
            data = request.POST
            username = data['email']
            password = data['password']
            
            user = authenticate(request, username=username, password=password)
            
            '''if user is not None and user.is_superuser:
                login(request, user=user)
                return redirect('admin:index')
            '''
            if user is not None:
                login(request, user=user)
                return redirect(dashboard)
            else:
            
                return render(request, 'home.html',{'msg':'Usuário ou senha incorreta'})
    return render(request, 'home.html',{})


def logout_user(request):
    logout(request)
    return redirect(aut_user)

'''
import asyncio

import schedule
import time

async def sorteioLoteria():
    print( 'testando2')
   

async def main():
    while 1:
        await asyncio.wait([schedule.every(10).seconds.do(sorteioLoteria)])
        
        #
        #schedule.run_pending()
        #await asyncio.sleep(1)
        time.sleep(1)
        
 

asyncio.run(main())
'''

from .models import Parametros
import random
import math

def dado(request):
    if request.method == 'POST':
        dado = request.POST['dado']
        if dado == 'd4':
            dado = list(range(1,5))
            return dado
        elif dado == 'd6':
            dado = list(range(1,7))
            return dado
        elif dado == 'd8':
            dado = list(range(1,9))
            return dado
        elif dado == 'd10':
            dado = list(range(1,11))
            return dado
        elif dado == 'd12':
            dado = list(range(1,13))
            return dado
        elif dado == 'd20':
            dado = list(range(1,21))
            return dado
        else:
            dado = list(range(1,101))
            return dado

    

def parametros(request):
    if request.method == 'POST':
        if request.POST['nd'] == '1/4':
            pk = 0
            return Parametros.objects.filter(pk=pk).values()
        elif request.POST['nd'] == '1/2':
            pk = 1
            return Parametros.objects.filter(pk=pk).values()
        else:
            return Parametros.objects.filter(pk=int(request.POST['nd'])+1).values()

def media_dano(request):
    if request.method == 'POST':
        ameaca = parametros(request).get()
        quantidade_dados = int(request.POST['quantidade_dados'])
        quantidade_ataques = int(request.POST['quantidade_ataques'])
        dados = dado(request)
        dano_medio = ameaca.get('dano_medio')

        minimo = int(min(dados))
        maximo = int(max(dados))
        media = math.floor((maximo+minimo)/2)*quantidade_dados
        modificador = math.floor((dano_medio - media)/quantidade_ataques)
        return modificador

def deslocamento(request):
    deslocamento = 9.0
    if request.method == 'POST':
        if (
            ((request.POST['deslocamento_tipo'] == 'Escalador' or request.POST['deslocamento_tipo'] == 'Escavador') and request.POST['delocamento_velocidade'] == 'Lento')
        or (request.POST['tamanho'] == 'Minúsculo' or request.POST['tamanho'] == 'Pequeno' and request.POST['deslocamento_tipo'] == 'Bípede' and request.POST['delocamento_velocidade'] == 'Lento')
        ):
            deslocamento = 4.5

        if ((request.POST['deslocamento_tipo'] == 'Escavador' and request.POST['delocamento_velocidade'] == 'Normal')
        or (request.POST['tamanho'] == 'Minúsculo' or request.POST['tamanho'] == 'Pequeno' and request.POST['deslocamento_tipo'] == 'Quadrúpede' and request.POST['delocamento_velocidade'] == 'Lento')
        or (request.POST['tamanho'] == 'Minúsculo' or request.POST['tamanho'] == 'Pequeno' and request.POST['deslocamento_tipo'] == 'Bípede' and request.POST['delocamento_velocidade'] == 'Normal')
        or (request.POST['tamanho'] == 'Médio' and request.POST['deslocamento_tipo'] == 'Bípede' and request.POST['delocamento_velocidade'] == 'Lento')
        ):
            deslocamento = 6.0

        if ((request.POST['deslocamento_tipo'] == 'Escalador' and request.POST['delocamento_velocidade'] == 'Rápida')
        or (request.POST['tamanho'] == 'Minúsculo' or request.POST['tamanho'] == 'Pequeno' and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Lento')
        or (request.POST['tamanho'] == 'Minúsculo' or request.POST['tamanho'] == 'Pequeno' and request.POST['deslocamento_tipo'] == 'Quadrúpede' and request.POST['delocamento_velocidade'] == 'Rápido')
        or (request.POST['tamanho'] == 'Médio' and request.POST['deslocamento_tipo'] == 'Quadrúpede' and request.POST['delocamento_velocidade'] == 'Normal')
        or (request.POST['tamanho'] == 'Médio' and request.POST['deslocamento_tipo'] == 'Bípede' and request.POST['delocamento_velocidade'] == 'Rápido')
        or ((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Bípede' and request.POST['delocamento_velocidade'] == 'Normal')
        or ((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Quadrúpede' and request.POST['delocamento_velocidade'] == 'Lento')
        ):
            deslocamento = 12.0

        if ((request.POST['deslocamento_tipo'] == 'Nadador' and request.POST['delocamento_velocidade'] == 'Normal')
        or (request.POST['tamanho'] == 'Minúsculo' or request.POST['tamanho'] == 'Pequeno' and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Normal')
        or (request.POST['tamanho'] == 'Médio' and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Lento')
        or (request.POST['tamanho'] == 'Médio' and request.POST['deslocamento_tipo'] == 'Quadrúpede' and request.POST['delocamento_velocidade'] == 'Rápido')
        or ((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Quadrúpede' and request.POST['delocamento_velocidade'] == 'Normal')
        or ((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Bípede' and request.POST['delocamento_velocidade'] == 'Rápido')
        ):
            deslocamento = 15.0

        if ((request.POST['tamanho'] == 'Minúsculo' or request.POST['tamanho'] == 'Pequeno' and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Rápido')
        or (request.POST['tamanho'] == 'Médio' and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Normal')
        or ((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Quadrúpede' and request.POST['delocamento_velocidade'] == 'Rápido')
        or ((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Lento')
        ):
            deslocamento = 18.0

        if ((request.POST['deslocamento_tipo'] == 'Nadador' and request.POST['delocamento_velocidade'] == 'Rápido')
        or (request.POST['tamanho'] == 'Médio' and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Rápido')
        or ((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Normal')
        ):
            deslocamento = 24.0
        if (((request.POST['tamanho'] == 'Grande' or request.POST['tamanho'] == 'Enorme' or request.POST['tamanho'] == 'Colossal') and request.POST['deslocamento_tipo'] == 'Voador' and request.POST['delocamento_velocidade'] == 'Rápido')
        ):
            deslocamento = 36.0
   
    return deslocamento 

def espaco(request):
    espaco_ocuapdo = 1.5
    if request.method == 'POST':
        if request.POST['tamanho'] == 'Grande':
            espaco_ocuapdo = 3.0
        if request.POST['tamanho'] == 'Enorme':
            espaco_ocuapdo = 4.5            
        if request.POST['tamanho'] == 'Colossal':
            espaco_ocuapdo = 6.0

    return espaco_ocuapdo

def manobras_furitividade(request):
    manobra = 0
    furitvidade = 0
    if request.method == 'POST':
        if request.POST['tamanho'] == 'Minúsculo':
            manobra = -5
            furitvidade = 5
        if request.POST['tamanho'] == 'Pequeno':
            manobra = -2
            furitvidade = 2
        if request.POST['tamanho'] == 'Grande':
            manobra = 2
            furitvidade = -2
        if request.POST['tamanho'] == 'Enorme':
            manobra = 5
            furitvidade = -5
        if request.POST['tamanho'] == 'Colossal':
            manobra = 10
            furitvidade = -10
    return '' + str(manobra) + '/' + str(furitvidade)
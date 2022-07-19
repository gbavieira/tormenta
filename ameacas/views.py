from django.shortcuts import render
from .forms import AmeacasForms
from .parametros import *

def index(request):
    form = AmeacasForms()
    dados = {'form':form}
    return render(request, 'index.html', dados)


def criar_ameaca(request):
    form = AmeacasForms()
    dados = {'form':form}
    return render (request, 'formulario.html', dados)

def criar_ameaca_aleatoria(request):
    return render (request, 'aleatoria.html')
    

def ameaca(request):
    if request.method == 'POST':
        form = AmeacasForms(request.POST)
        if form.is_valid():
            ameaca = parametros(request).get()
            bonus_ataque = ameaca.get('bonus_ataque')
            dano_medio = ameaca.get('dano_medio')
            defesa = ameaca.get('defesa')
            resis_forte = ameaca.get('resis_forte')
            resis_media = ameaca.get('resis_media')
            resis_fraca = ameaca.get('resis_fraca')
            pv = ameaca.get('pv')
            cd = ameaca.get('cd')
            nd = ameaca.get('nd')

            modificador = media_dano(request)
            andar = deslocamento(request)
            espaco_ocupado = espaco(request)
            mod_manobra_furtividade = manobras_furitividade(request)

            dados = {
                'form':form,
                'nd':nd,
                'bonus_ataque': bonus_ataque,
                'dano_medio': dano_medio,
                'defesa':defesa,
                'resis_forte':resis_forte,
                'resis_media':resis_media,
                'resis_fraca':resis_fraca,
                'pv':pv,
                'cd':cd,
                'modificador':modificador,
                'andar':andar,
                'espaco_ocupado':espaco_ocupado,
                'mod_manobra_furtividade':mod_manobra_furtividade,
            }
            
            return render(request, 'ameaca.html', dados)
        else:
            form = AmeacasForms()
            dados = {'form':form}
            print(form.errors)
            return render(request, 'formulario.html',dados)
    else:
        form = AmeacasForms()
        dados = {'form':form}
        return render (request, 'formulario.html', dados)

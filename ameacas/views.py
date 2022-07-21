from django.shortcuts import render
from .forms import AmeacasForms, AmeacasAleatoriasForm
from .parametros import *
from .aleatorias import *

def index(request):
    form_aleatoria = AmeacasAleatoriasForm()
    dados = {'form_aleatoria':form_aleatoria}
    return render(request, 'index.html', dados)


def criar_ameaca(request):
    form = AmeacasForms()
    dados = {'form':form}
    return render (request, 'formulario.html', dados)


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

def criar_ameaca_aleatoria(request):
    nd = nd_form(request)
    attr = atributos(request)
    tam = tamanho(request)
    peri = per(request)
    ameaca = parametros(request).get()
    defesa = ameaca.get('defesa')
    pv = ameaca.get('pv')
    cd = ameaca.get('cd')
    pm = mana(request)
    andar = deslocamento_aleatorio(request)

    # Condições de resistências para cada conceito
    if attr['conc'] == 'Combatente':
        peri['fort'] = ameaca.get('resis_forte')
        peri['refl'] = ameaca.get('resis_media')
        peri['vont'] = ameaca.get('resis_fraca')
    elif attr['conc'] == 'Arcano':
        peri['vont'] = ameaca.get('resis_forte')
        peri['refl'] = ameaca.get('resis_media')
        peri['fort'] = ameaca.get('resis_fraca')
    else:
        peri['refl'] = ameaca.get('resis_forte')
        peri['vont'] = ameaca.get('resis_media')
        peri['fort'] = ameaca.get('resis_fraca')

    # Condições de melhorias de perícias para cada conceito
    if nd in iniciante:
        if attr['conc'] == 'Velocista' or attr['conc'] == 'Combatente':
            peri['inic'] = peri['inic']+5
        else:
            peri['perc'] = peri['perc']+2
            peri['mist'] = peri['mist']+5
    if nd in veterano:
        if attr['conc'] == 'Velocista' or attr['conc'] == 'Combatente':
            peri['inic'] = peri['inic']+10
        else:
            peri['perc'] = peri['perc']+5
            peri['mist'] = peri['mist']+10
    if nd in campeao or nd in lenda:
        if attr['conc'] == 'Velocista' or attr['conc'] == 'Combatente':
            peri['inic'] = peri['inic']+15
        else:
            peri['perc'] = peri['perc']+10
            peri['mist'] = peri['mist']+15

    if nd == 0.5:
        nd = '1/2'
    elif nd == 0.25:
        nd = '1/4'
    criatura = {
        'tam':tam,
        'nd':nd,
        'attr': attr,
        'peri':peri,
        'defesa':defesa,
        'pv':pv,
        'cd':cd,
        'pm':pm,
        'andar':andar,
    }
    return render (request, 'aleatoria.html', criatura)
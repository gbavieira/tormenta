import random
import math


tamanho_lista = ['Minúsculo','Pequeno','Médio','Grande','Enorme','Colossal']
conceito = ['Combatente','Arcano','Velocista']
pericias = [
    'acro','ades','atle','atua','cava','conh','cura','dipl','enga','fort','furt',
    'guer', 'inic', 'inti', 'intu', 'inve','joga','ladi','luta','mist','nobr','ofic',
    'perc', 'pilo', 'pont', 'refl', 'reli', 'sobr', 'vont',
]
incapaz = 1
incompetente = [2,3,4,5]
ineficaz = [6,7,8,9]
mediano = [10,11,12,13]
notavel = [14,15,16,17]
excelente = [18,19,20,21]
extraordinario = [22,23,24,25]
excepcional = [26,27,28,29,30,31,32]

iniciante = [0.25,0.5,1,2,3,4]
veterano = [5,6,7,8,9,10]
campeao = [11,12,13,14,15,16]
lenda = [17,18,19,20]

def nd_form(request):
    if request.method == 'POST':
        if request.POST['nd'] == '1/4':
            nd = 0.25
        elif request.POST['nd'] == '1/2':
            nd = 0.5
        else:
            nd = int(request.POST['nd'])
    return nd

def tamanho(request):
    tamanho_criatura = random.choice(tamanho_lista)
    return tamanho_criatura

def atributos(request):
    conc = random.choice(conceito)
    if conc == 'Arcano':
        tipo_criatura = ["Construto","Espírito","Humanóide"]
        model = random.choice(tipo_criatura)
    elif conc == 'Velocista':
        tipo_criatura = ["Animal","Espírito","Humanóide","Monstro","Morto-Vivo"]
        model = random.choice(tipo_criatura)
    else:
        tipo_criatura = ["Animal","Construto","Espírito","Humanóide","Monstro","Morto-Vivo"]
        model = random.choice(tipo_criatura)
    
    nd = nd_form(request)

    if nd in iniciante:
        if conc == 'Combatente':
            forca = random.choice(excelente)
            des = random.choice(notavel)
            con = random.choice(notavel)
            intel = random.choice(mediano)
            sab = random.choice(ineficaz)
            car = random.choice(mediano)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Construto' or model == 'Morto-Vivo':
                intel = incapaz
            elif model == 'Monstro':
                con = random.choice(excelente)
                intel = random.choice(incompetente)
        elif conc == 'Arcano':
            forca = random.choice(ineficaz)
            des = random.choice(mediano)
            con = random.choice(mediano)
            intel = random.choice(excelente)
            sab = random.choice(notavel)
            car = random.choice(mediano)
            if model == 'Construto':
                con = random.choice(notavel)
        else:
            forca = random.choice(mediano)
            des = random.choice(excelente)
            con = random.choice(mediano)
            intel = random.choice(notavel)
            sab = random.choice(ineficaz)
            car = random.choice(ineficaz)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Morto-Vivo':
                intel = incapaz
            elif model == 'Monstro':
                con = random.choice(excelente)
                car = random.choice(incompetente)
                intel = random.choice(incompetente)
    
    elif nd in veterano:
        if conc == 'Combatente':
            forca = random.choice(extraordinario)
            des = random.choice(notavel)
            con = random.choice(excelente)
            intel = random.choice(mediano)
            sab = random.choice(ineficaz)
            car = random.choice(mediano)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Construto' or model == 'Morto-Vivo':
                intel = incapaz
            elif model == 'Monstro':
                con = random.choice(extraordinario)
                intel = random.choice(incompetente)
        elif conc == 'Arcano':
            forca = random.choice(ineficaz)
            des = random.choice(mediano)
            con = random.choice(notavel)
            intel = random.choice(extraordinario)
            sab = random.choice(notavel)
            car = random.choice(mediano)
            if model == 'Construto':
                con = random.choice(excelente)
        else:
            forca = random.choice(notavel)
            des = random.choice(extraordinario)
            con = random.choice(mediano)
            intel = random.choice(excelente)
            sab = random.choice(mediano)
            car = random.choice(ineficaz)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Morto-Vivo':
                intel = incapaz
            elif model == 'Monstro':
                forca = random.choice(excelente)
                con = random.choice(excelente)
                sab = random.choice(ineficaz)
                intel = random.choice(incompetente)
    
    elif nd in campeao:
        if conc == 'Combatente':
            forca = random.choice(extraordinario)
            des = random.choice(excelente)
            con = random.choice(extraordinario)
            intel = random.choice(mediano)
            sab = random.choice(ineficaz)
            car = random.choice(mediano)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Construto' or model == 'Morto-Vivo':
                intel = incapaz
        elif conc == 'Arcano':
            forca = random.choice(mediano)
            des = random.choice(notavel)
            con = random.choice(notavel)
            intel = random.choice(extraordinario)
            sab = random.choice(excelente)
            car = random.choice(notavel)
            if model == 'Construto':
                con = random.choice(excelente)
        else:
            forca = random.choice(notavel)
            des = random.choice(extraordinario)
            con = random.choice(notavel)
            intel = random.choice(excelente)
            sab = random.choice(mediano)
            car = random.choice(mediano)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Morto-Vivo':
                intel = incapaz
            elif model == 'Monstro':
                forca = random.choice(excelente)
                con = random.choice(excelente)
                sab = random.choice(ineficaz)
                car = random.choice(ineficaz)
                intel = random.choice(ineficaz)

    else:
        if conc == 'Combatente':
            forca = random.choice(excepcional)
            des = random.choice(extraordinario)
            con = random.choice(extraordinario)
            intel = random.choice(notavel)
            sab = random.choice(ineficaz)
            car = random.choice(mediano)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Construto' or model == 'Morto-Vivo':
                intel = incapaz
        elif conc == 'Arcano':
            forca = random.choice(mediano)
            des = random.choice(notavel)
            con = random.choice(notavel)
            intel = random.choice(excepcional)
            sab = random.choice(extraordinario)
            car = random.choice(excelente)
            if model == 'Construto':
                con = random.choice(excepcional)
        else:
            forca = random.choice(excelente)
            des = random.choice(excepcional)
            con = random.choice(notavel)
            intel = random.choice(excelente)
            sab = random.choice(mediano)
            car = random.choice(mediano)
            if model == 'Animal':
                intel = random.choice([1,2])
            elif model == 'Morto-Vivo':
                intel = incapaz
            elif model == 'Monstro':
                forca = random.choice(excelente)
                con = random.choice(excepcional)
                sab = random.choice(ineficaz)
                car = random.choice(ineficaz)
                intel = random.choice(ineficaz)
            
    return {
        'forca':forca,
        'des':des,
        'con':con,
        'intel':intel,
        'sab':sab,
        'car':car,
        'model':model,
        'conc':conc,
    }

def per(request):
    nd = nd_form(request)
    pericias_valores = []
    for i in pericias:
        pericias_valores.append(i)
        pericias_valores.append(math.floor(nd/2))
        
    pericias_valores = dict(zip(i := iter(pericias_valores), i ))

    return pericias_valores

def mana(request):
    nd = nd_form(request)
    if nd < 1:
        pm = 3
    pm = nd*3
    return pm

def deslocamento_aleatorio(request):
    deslocamento = random.choice([6,9,12])
    return deslocamento

from django import forms

DADO_CHOICES = [('','Tipo de Dado'),('d4','d4'),('d6','d6'),('d8','d8'),('d10','d10'),('d12','d12'),('d20','d20'),('d100','d100')]
ND_CHOICES = [('','ND'),('1/4','1/4'),('1/2','1/2'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),
    ('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),
    ('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),]
DESLOCAMENTO_TIPO_CHOICES = [('','Tipo de Deslocamento'),('Bípede','Bípede'),('Quadrúpede','Quadrúpede'),('Voador','Voador'),
    ('Escalador','Escalador'),('Escavador','Escavador'),('Nadador','Nadador')]
DESLOCAMENTO_VELOCIDADE_CHOICES = [('','Velocidade do Deslocamento'),('Lento','Lento'),('Normal','Normal'),('Rápido','Rápido'),]
TAMANHO_CHOICES = [('','Tamanho'),('Minúsculo','Minúsculo'),('Pequeno','Pequeno'),('Médio','Médio'),('Grande','Grande'),
    ('Enorme','Enorme'),('Colossal','Colossal')]

class AmeacasForms(forms.Form):
    quantidade_ataques = forms.IntegerField(max_value=5,min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Quantidade de Ataques (Entre 1 e 5)'}),required=True)
    quantidade_dados = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={'placeholder': 'Quantidade de Dados'}),required=True)
    dado = forms.ChoiceField(choices=DADO_CHOICES, required=True)
    nd = forms.ChoiceField(choices=ND_CHOICES, required=True)
    deslocamento_tipo = forms.ChoiceField(choices=DESLOCAMENTO_TIPO_CHOICES, required=True)
    delocamento_velocidade = forms.ChoiceField(choices=DESLOCAMENTO_VELOCIDADE_CHOICES, required=True)
    tamanho = forms.ChoiceField(choices=TAMANHO_CHOICES, required=True)

class AmeacasAleatoriasForm(forms.Form):
    nd = forms.ChoiceField(choices=ND_CHOICES, required=True)
    


    


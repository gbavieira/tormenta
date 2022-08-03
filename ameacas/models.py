from django.db import models
from django.utils.translation import gettext as _

class Parametros(models.Model):
    nd = models.CharField(_("nd"),max_length=10,)
    bonus_ataque = models.IntegerField(_("bonus_ataque"))
    dano_medio = models.IntegerField(_("dano_medio"))
    defesa = models.IntegerField(_("defesa"))
    resis_forte = models.IntegerField(_("resis_forte"))
    resis_media = models.IntegerField(_("resis_media"))
    resis_fraca = models.IntegerField(_("resis_fraca"))
    pv = models.IntegerField(_("pv"))
    cd = models.IntegerField(_("cd"))

class Poderes(models.Model):
    nome_poder = models.CharField(_("nome_poder"),max_length=100,)


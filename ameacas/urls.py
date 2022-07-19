from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('ameaca',ameaca, name='ameaca'),
    path('criar-ameaca',criar_ameaca, name='criar-ameaca'),
    path('criar-ameaca-aleatoria',criar_ameaca_aleatoria, name='criar-ameaca-aleatoria'),
]
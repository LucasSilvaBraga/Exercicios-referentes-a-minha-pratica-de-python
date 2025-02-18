#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM,
#COBRANDO R$0.50 POR KM PARA VIAGENS DE ATÉ 200KM E R$0.45 PARA VIAGENS MAIS LONGES 

from random import choice

Destino = choice(list(range(50 ,250)))

if Destino > 200:
    Custo = Destino * 0.45
else:
    Custo = Destino * 0.50

print('Seu destino fica a {} kms, portanto o custo da passagem sera de {:.2f}'. format(Destino, Custo))
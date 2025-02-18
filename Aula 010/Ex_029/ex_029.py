#ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO. 
# A MULTA VAI CUSTAR R$7.00 POR CADA KM ACIMA DO LIMITE.

from random import choice

Velocidade = list(range(60, 140))
Velocidade = choice(Velocidade)


if Velocidade > 80:
    print('Voce ultrapassou o limite de velocidade sua multa eh de: {} reais'. format((Velocidade - 80) * 7 ))
else:
    print('Velocidade de acordo com a lei, prossiga')


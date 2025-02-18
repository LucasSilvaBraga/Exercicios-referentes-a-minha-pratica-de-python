#====CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMRPAR. CONSIDERE US$1,00 = R$3,27====

Dinheiro = float(input('Digite a quantidade de dinheiro atual: '))

print('A quantidade de dinheiro em dolares eh: {:.2f}'. format(Dinheiro / 3.27))

#'{:.2f}' limita em duas casas a exibicao do valor desejado, lembrando que o python arredonda o valor
#ex: se o valor eh: 6.116207951070336 ele sera transformado em: 6.12
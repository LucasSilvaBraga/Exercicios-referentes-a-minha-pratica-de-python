#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA  A SUA PORÇÃO INTEIRA 
#Ex: Digite um número: 1.676 ---> o numero 1.676 tem parte inteira em 1.

Numero = float(input('Digite um numero real qualquer: '))

print('A porcao inteira desse numero eh: {}'. format(Numero // 1))
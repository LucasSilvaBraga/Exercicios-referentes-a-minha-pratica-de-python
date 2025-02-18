#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA  A SUA PORÇÃO INTEIRA 
#Ex: Digite um número: 1.676 ---> o numero 1.676 tem parte inteira em 1.

from math import trunc #Digitar a sintaxe: from 'biblioteca' import 'funcao' fara com que nao precisemos nos referenciar a um objeto apenas utilizando suas funcoes diretamente

Numero = float(input('Digite um numero: '))
print('A parte inteira desse numero eh: {}'. format(trunc(Numero)))
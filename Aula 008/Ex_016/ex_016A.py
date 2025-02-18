#CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO E MOSTRE NA TELA  A SUA PORÇÃO INTEIRA 
#Ex: Digite um número: 1.676 ---> o numero 1.676 tem parte inteira em 1.

import math #Importando a biblioteca math

Numero = float(input('Digite um numero: '))

print('A parte inteira desse numero eh: {}'. format(math.trunc(Numero)))
#A funcao 'trunc' da biblioteca 'math' retira apenas a parte inteira de um numero

#Preceba que ao importar uma biblioteca estamos rabalhando com oriantacao a objetos
#'math' age como objeto, 'trunc' como uma de suas funcoes e 'Numero' como o argumento dessa funcao
#lembrando que um objeto e uma instancia de uma classe 
#Em linguagem c nos mesmos criamos nossos proprios objetos que ja recebem seus proprios atributos atraves de suas funcoes


#ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR 'PENSAR' EM UM NÚMERO INTEIRO ENTRE 0 E 5 E PEÇA PARA O USU´RIO TENTAR DESCOBRIR
#QUAL FOI O NUMERO ESCOLHIDO PELO COMPUTADOR. O PROGRAMA TAMBÉM DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU

from random import choice

Numeros = [0, 1, 2, 3, 4, 5]
Numeros = choice(Numeros)

Numero1 = int(input("Eu pensei em um numero de 0 a 5 tente advinhar qual eh: "))

#Em python os condicionais sao orientados a partir da identacao,
#O argumento do condicional pode ser adicionado entre ele e os ':'  
if Numero1 == Numeros:
    print('Voce acertou eu havia pensado no numero {}'. format(Numeros))
else:
    print("Voce errou eu havia pensado no numero {}". format(Numeros))


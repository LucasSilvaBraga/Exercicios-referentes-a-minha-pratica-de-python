#Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10. So que agora o jogador vai tentar adivinhar ate acertar,
# mostrando no final quantos palpites foram necessarios para vencer

from random import choice

Contador = 0

NumeroSorteado = choice(list(range(0, 10)))

NumeroEscolhido = int(input("O computador sorteou um numero, tente advinhar qual eh: "))

while NumeroEscolhido != NumeroSorteado:
    if NumeroEscolhido > NumeroSorteado:
        Contador += 1
        print("...O numero eh um pouco menor...")
        NumeroEscolhido = int(input("Tente escolher outro numero: "))
    if NumeroEscolhido < NumeroSorteado:
        Contador += 1
        print("...O numero eh um pouco maior...")
        NumeroEscolhido = int(input("Tente escolher outro numero: "))
 
Contador += 1
print("Acertou!!! O numero sorteado era: {}". format(NumeroSorteado))
print("Voce acertou em {} tentativas". format(Contador))

    


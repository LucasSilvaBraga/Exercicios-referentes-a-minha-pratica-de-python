#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla

from random import randint

Maior = 0
Menor = 99999999999

NumerosSorteados = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))

print("Os numeros gerados foram: ", end = '')

for i in range(0, 5):
    print(f"{NumerosSorteados[i]} ", end = '')
    if NumerosSorteados[i] > Maior:
        Maior = NumerosSorteados[i]
    if NumerosSorteados[i] < Menor:
        Menor = NumerosSorteados[i]

print(f"\nO menor numero sorteado foi: {Menor}")
print(f"O maior numero sorteado foi: {Maior}")

#Tuplas tambem possuem a funcao min e max que indicam qual e o menor e maior numero
print(min(NumerosSorteados))
print(max(NumerosSorteados))

    


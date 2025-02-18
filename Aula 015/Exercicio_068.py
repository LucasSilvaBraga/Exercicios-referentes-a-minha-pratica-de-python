#Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador perder,
# mostrando o total de vitorias consecutivas que ele conquistou o final do jogo

from time import sleep
from random import choice

Escolha  = ''
Contador = 0

while True:
    Escolha = input("Par ou impar? ").upper()
    Numeros = float(input("Quantos dedos voce mostra? "))
    NumerosComputador = choice(list(range(0, 10)))
    
        

    print("Um")
    sleep(1)
    print("Do")
    sleep(1)
    print("La")
    sleep(1)
    print("Si")
    sleep(1)
    print("JA!!!")
    print(f"Computador: {NumerosComputador}\nUsuario: {Numeros}")
    sleep(1)
    if Escolha == 'PAR' and (NumerosComputador + Numeros) % 2 == 0:
        Contador += 1
        print("Vitoria do usuario!!!")
        print(f"Quantidade de vitorias: {Contador}")
    elif Escolha == 'IMPAR' and (NumerosComputador + Numeros) % 2 != 0:
        Contador += 1
        print("Vitoria do usuario!!!")
        print(f"Quantidade de vitorias: {Contador}")
    else:
        print("Vitoria do computador!!!")
        print(f"Total de vitorias do usuario: {Contador}")
        break

    


#Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. 
# O programa sera interrompido quando o numero solicitado for negativo

Numeros = 0

while True:
    Numeros = int(input("Digite um numero para que sua respectiva tabuada seja mostrada (digite um numero menor que 0 para sair): "))

    if Numeros < 0:
        break

    print(f"{Numeros} x 1 = {Numeros * 1}")
    print(f"{Numeros} x 2 = {Numeros * 2}")
    print(f"{Numeros} x 3 = {Numeros * 3}")
    print(f"{Numeros} x 4 = {Numeros * 4}")
    print(f"{Numeros} x 5 = {Numeros * 5}")
    print(f"{Numeros} x 6 = {Numeros * 6}")
    print(f"{Numeros} x 7 = {Numeros * 7}")
    print(f"{Numeros} x 8 = {Numeros * 8}")
    print(f"{Numeros} x 9 = {Numeros * 9}")
    print(f"{Numeros} x 10 = {Numeros * 10}")




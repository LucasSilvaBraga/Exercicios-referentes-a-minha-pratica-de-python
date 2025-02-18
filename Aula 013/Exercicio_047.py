#Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500

Contagem = 0

for i in range (0, 501, 3):
    if i % 2 > 0:
        Contagem = i + Contagem
    print(Contagem)


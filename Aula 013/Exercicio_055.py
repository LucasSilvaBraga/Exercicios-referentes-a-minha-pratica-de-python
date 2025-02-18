#Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

Maior = 0
Menor = 10000000000000000

for i in range (0, 5):
    Peso = int(input("Digite o peso da pessoa [{}]". format(i + 1)))
    if Peso > Maior:
        Maior = Peso
    if Peso < Menor:
        Menor = Peso

print("O maior peso lido foi de {}Kg". format(Maior))
print("O menor peso lido foi de {}Kg". format(Menor))







#Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao

PrimeiroTermo = int(input("Digite o primeiro termo da PA: "))
Razao = int(input("Digite a razao dessa PA: "))

PrimeiroTermo + Razao

for i in range(0, 10,):
    print("{} -> ". format(PrimeiroTermo), end='')
    PrimeiroTermo = PrimeiroTermo + Razao
print("Acabou")
#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidereos

Soma = 0

for i in range(0, 7):
    Numero = int(input(("Digite um numero[{}]: ". format(i+1))))
    if Numero % 2 == 0:
        Soma = Numero + Soma

print("O resultado da soma dos numeros digitados eh: {}". format(Soma))
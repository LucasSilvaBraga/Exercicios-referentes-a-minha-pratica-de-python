#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999,
# que eh a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

Numeros = 0
Soma = 0
Contador = 0

while Numeros != 999:
    Numeros = int(input("Digite um numero: "))
    if Numeros != 999:
        Contador += 1
        Soma = Numeros + Soma

print("Quantidade de numeros digitado: {}\nSoma entre os numeros digitados: {}". format(Contador, Soma))




#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que eh a condicao de parada.
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando a flag)

Soma = 0
Numeros = 0
Contador = 0

while True:
    Numeros = int(input("Digite um numero(999 para sair): "))
    if Numeros == 999:
        print(f"A soma entre os numeros digitados foi de: {Soma}")
        print(f"Quantidade de valores digitados: {Contador}")
        break
    Soma += Numeros
    Contador += 1

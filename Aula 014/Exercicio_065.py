#Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao mostre a media entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores

Continuar = 'S'

Numeros = 0
Maior = 0
Menor = 9999999999999999999999999999
Contador = 0
Soma = 0

while Continuar == 'S':
    Numeros = int(input("Digite um numero: "))

    #Maior e menor
    if Numeros > Maior:
        Maior = Numeros
    if Numeros < Menor:
        Menor = Numeros

    #Soma  e contador para fazer a media posteriormente
    Soma = Numeros + Soma
    Contador += 1

    #Verificacao para contiuar
    Continuar = input("Deseja continuar (S/N): ").upper()

Media = Soma / Contador

print("Maior numero digitado: {}\nMenor numero digitado: {}\nMedia entre os valores digitados: {}". format(Maior, Menor, Media))






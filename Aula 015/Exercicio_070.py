#Crie um programa que leia o nome e o preco de varias produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre
#Qual eh o total gasto na compra
#Quantos produtos custam mais de R$1000
#Qual eh o nome do produto mais barato

Nome = ''
MaisBarato = 99999999999999999999999999
Total = 0
Total1000 = 0
Resposta = ''

while True:
    Nome = input("Digite o nome do produto: ")
    Preco = float(input("Digite o preco do produto: "))

    Total += Preco
    if Preco < MaisBarato:
        MaisBarato = Preco
        NomeMaisBarato = Nome
    if Preco > 1000:
        Total1000 += 1

    Resposta = input("Deseja continuar(s/n): ").upper()
    print(f"A resposta foi: {Resposta}")

    if Resposta == 'N':
        print(f"O total gasto na compra foi: {Total}")
        print(f"O total de prdutos que custaram mais de R$1000 foi de: {Total1000}")
        print(f"O produto mais barato foi: {NomeMaisBarato}")
        break




#====FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO====


Preco = float(input('Digite o preco do produto: '))

PrecoFinal = Preco - (Preco * 0.05)

print('O preco final do produto eh: {}'. format(PrecoFinal))
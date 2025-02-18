#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
#A vista dinheiro/cheque: 10% de desconto
#A vista no cartao: 5% de desconto
#Em ate 2x no cartao: preco normal
#3x ou mais no cartao: 20% de juros

Valor = float(input("Digite o valor do produto:"))
Metodo = int(input("Selecione o metodo de pagamento:\n[1]A vista ou cheque\n[2]A vista no cartao\n[3]2x no cartao\n[4]3x no cartao\n "))

if Metodo == 1:
    print("O valor do produto eh: {}". format(Valor - (Valor * 0.10)))
elif Metodo == 2:
    print("O valor do produto eh: {}". format(Valor -(Valor * 0.5)))
elif Metodo == 3:
    print("O produto foi parcelado em 2x de {}". format(Valor / 2))
elif Metodo == 4:
    print("O produto foi parcelado em 3x de: {}". format((Valor * 1.20) / 3))





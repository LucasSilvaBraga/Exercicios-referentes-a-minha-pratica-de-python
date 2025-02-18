#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre  quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores

from datetime import datetime

AnoAtual = datetime.now()
AnoAtual = AnoAtual.year

#Mesmo nao tendo que declarar o tipo da variavel temos que declarar
Maioridade = 0
Menoridade = 0

for i in range (0, 7, 1):
    Ano = int(input("Digite o ano de nascimento da pessoa [{}]: ". format(i + 1)))
    Resultado = AnoAtual - Ano
    if Resultado > 19:
        Maioridade = Maioridade + 1
    else:
        Menoridade = Menoridade + 1

print("{} pessoas na maioridade\n{} pessoas na menoridade". format(Maioridade, Menoridade))




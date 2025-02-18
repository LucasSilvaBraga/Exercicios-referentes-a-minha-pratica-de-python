#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci
#Lmebrando que a o proximo numero da sequencia de fibonacci e sempre a soma dos dois ultimos numeros

Contador = int(input("Digite a quantidade de termos da sua sequencia de fibonacci: "))
TermoAtual = 1
TermoPassado = 0

print("{} -> ". format(TermoPassado), end = '')
while Contador > 1:
    print("{} -> ". format(TermoAtual), end = '')
    Temp = TermoAtual
    TermoAtual = TermoAtual + TermoPassado
    TermoPassado = Temp
    Contador -= 1

print("Fim")


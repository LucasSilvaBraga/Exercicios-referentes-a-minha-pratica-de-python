#Faca um programa que leia um numero inteiro e diga se ele eh ou nao um numero primo

Numero = int(input("Digite um numero para ser verificado: "))
VerificacaoPrimo = 0

for i in range(1, Numero + 1):
    Resultado = Numero % i
    if Resultado == 0:
       VerificacaoPrimo = VerificacaoPrimo + 1
       print("{} / {} TIVERAM DIVISAO EXATA!". format(Numero, i))
    else:
        print("{} / {} nao tiveram divisao exata!". format(Numero, i))

if VerificacaoPrimo == 2:
    print("{} eh primo". format(Numero))
else:
    print("{} nao eh primo". format(Numero))

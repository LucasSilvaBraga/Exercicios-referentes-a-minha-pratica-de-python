#ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
#O PRIMEIRO VALOR É MAIOR
#O SEGUNDO VALOR É MAIOR
#NÃO EXISTE VALOR MAIOR OS DOIS SÃO IGUAIS

Numero1 = int(input("Digite o primeiro numero inteiro: "))
Numero2 = int(input("Digite  o segundo numero inteiro: "))

#-----Primeira resolucao possivel-----
if Numero1 > Numero2:
    print("O primeiro valor eh maior")
elif Numero2 > Numero1:
    print("O segundo valor eh maior")
else:
    print("Nao existe valor maior os dois sao iguais")


#-----Segunda resolucao possivel-----

#if Numero1 > Numero2:
#    print("O primeiro numero eh maior")
#if Numero2 > Numero1:
#    print("O segundo numero eh maior")
#if Numero1 == Numero2:
#   print("Nao existe numero maior os dois sao iguais")


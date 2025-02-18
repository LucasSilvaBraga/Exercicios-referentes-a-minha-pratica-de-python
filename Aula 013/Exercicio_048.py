#Refaca o exercicio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for.

Opcao = int(input("Qual tabuada deseja consultar?\n"))

for i in range(0, 11):
    print("{} X {} = {}". format(Opcao, i, (Opcao * i)))

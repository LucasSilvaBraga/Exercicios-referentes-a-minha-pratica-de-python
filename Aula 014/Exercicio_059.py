#Crie um programa que leia dois valores e mostre um menu o abaixo
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
#Seu programa devera realizar a operacao solicitada em cada caso 

Opcao = 0

Numero1 = int(input("Digite dois numeros inteiros\nPrimeiro numero:"))
Numero2 = int(input("Segundo numero: "))

while(Opcao != 5):
    Opcao = int(input("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Numeros\n[5] Sair do programa\n"))

    if Opcao == 1:
        print("{} + {} = {}". format(Numero1, Numero2, Numero1 + Numero2))
    elif Opcao == 2:
        print("{} x {} = {}". format(Numero1, Numero2, Numero1 * Numero2))
    elif Opcao == 3:
        if Numero1 > Numero2:
            print("O maior numero eh: {}". format(Numero1))
        elif Numero2 > Numero1:
            print("O maior numero eh: {}". format(Numero2))
        else:
            print("Os numeros sao iguais!")
    elif(Opcao == 4):
        Numero1 = int(input("Digite dois numeros inteiros\nPrimeiro numero:"))
        Numero2 = int(input("Segundo numero: "))
    

print("Programa encerrado")
    

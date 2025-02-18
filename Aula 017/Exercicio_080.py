#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

Lista = []
PosicaoUltimoMenor = 0

for i in range(0, 5):
    Numero = int(input("Digite o numero que deseja adicionar: "))
    PosicaoUltimoMenor = 0
    for j in range(0, len(Lista)):
        if Numero > Lista[j]:
            PosicaoUltimoMenor = j + 1
    Lista.insert(PosicaoUltimoMenor, Numero)
    
print(Lista)








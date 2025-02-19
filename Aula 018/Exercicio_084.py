#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

FlagContinuar = ''
MatrizPessoas = []
ListaPessoa = []
MatrizMaisPesados = []
MatrizMaisLeves = []

while FlagContinuar != 'n':
    ListaPessoa.clear()

    #Inserindo os dados de um individuo numa lista simples
    ListaPessoa.insert(0, input("Digite o nome da pessoa: "))
    ListaPessoa.insert(1, input("Digite o peso dessa pessoa: "))

    #Primeiro caso: Ja ha valores no ranking de mais leves ou mais pesados

    #Matriz mais pesados
    if len(MatrizMaisPesados) > 0:
        Contador = len(MatrizMaisPesados) -1
        while Contador != -1:
            if MatrizMaisPesados[Contador][1] > ListaPessoa[1]:
                MatrizMaisPesados.insert(Contador + 1, ListaPessoa[:])
                print(f"Matriz mais pesados1: {MatrizMaisPesados}")
                break
            Contador -= 1
        if Contador == -1:
            MatrizMaisPesados.append(ListaPessoa[:])
            print(f"Matriz mais pesados2: {MatrizMaisPesados}")

    #Matriz mais leves
    if len(MatrizMaisLeves) > 0:
        Contador = 0
        while Contador != len(MatrizMaisLeves):
            if MatrizMaisPesados[Contador][1] > ListaPessoa[1]:
                MatrizMaisLeves.insert(Contador , ListaPessoa[:])
                print(f"Matriz mais leves1: {MatrizMaisLeves}")
                break
            Contador += 1
        if Contador == len(MatrizMaisLeves):
            MatrizMaisLeves.insert(0, ListaPessoa[:])
            print(f"Matriz mais leves2: {MatrizMaisLeves}")

    #Segundo caso: nenhum valor no ranking de mais leves ou mais pesados foi incluido ainda
    if len(MatrizMaisPesados) == 0:
        MatrizMaisPesados.append(ListaPessoa[:])
        print(f"Matriz mais pesados3: {MatrizMaisPesados}")
    if len(MatrizMaisLeves) == 0:
        MatrizMaisLeves.append(ListaPessoa[:])
        print(f"Matriz mais leves3: {MatrizMaisLeves}")
    
    
    #Verificando se o usuario deseja continuar digitando valores
    FlagContinuar = input("Deseja continuar cadastrando pessoas? (s/n): ").lower()
    if FlagContinuar in 'n':
        break
    elif FlagContinuar not in 'ns':
        FlagContinuar = input("Digite uma resposta valida. Deseja continuar cadatrando pessoas? (s/n):").lower()

print(f"Matriz mais leves {MatrizMaisLeves}")
print(f"Matriz mais pesados {MatrizMaisPesados}")


#Pesquisar depois o funcionamento da flag continuar
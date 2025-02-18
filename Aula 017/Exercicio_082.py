#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

#Inicializando as variaveis
Lista = []
ListaPar = []
ListaImpar = []

while True:

    #Bloco para adicionar os numeros em cada uma das listas 
    Numero = int(input("Digite um numero para ser adicionado a lista: "))
    Lista.append(Numero)
    if Numero % 2 == 0:
        ListaPar.append(Numero)
    else:
        ListaImpar.append(Numero)


    #Bloco para verificar se o usuario deseja continuar a digitar valores
    FlagContinuar = input("Deseja coninuar a digitar valores? (s/n):")
    while FlagContinuar not in 'SsNn':
        FlagContinuar = input("Digite uma resposta valida (s/n): ")
    if FlagContinuar in 'nN':
        break

print(f"Todos os numeros digitados foram: {Lista}")
print(f"Os numeros pares digitados foram: {ListaPar}")
print(f"Os numeros impares digitados foram: {ListaImpar}")

  



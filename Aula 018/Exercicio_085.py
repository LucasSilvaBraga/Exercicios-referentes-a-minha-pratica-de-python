#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

ListaNumeros = []
ListaPares = []
ListaImpares = []
Contador = 0

for i in range(0, 7):

    Numeros = int(input(f"Digite o valor numero [{i + 1}]: "))
    if Numeros % 2 == 0:
        if len(ListaPares) == 0:
            ListaPares.append(Numeros)
        else:
            Contador = 0
            while Contador != len(ListaPares):
                if ListaPares[Contador] > Numeros:
                    ListaPares.insert(Contador, Numeros)
                    break
                Contador += 1
            if Contador == len(ListaPares):
                ListaPares.append(Numeros)
    else:
        if len(ListaImpares) == 0:
            ListaImpares.append(Numeros)
        else:
            Contador = 0
            while Contador != len(ListaImpares):
                if ListaImpares[Contador] > Numeros:
                    ListaImpares.insert(Contador, Numeros)
                    break
                Contador += 1
            if Contador == len(ListaImpares):
                ListaImpares.append(Numeros)
ListaNumeros = [ListaPares, ListaImpares]

print(f"Numeros pares digitados: {ListaNumeros[0]}\n Numeros impares digitados: {ListaNumeros[1]}")





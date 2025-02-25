#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

Matriz = []
Lista = []
SomaPares = 0
SomaColunas = 0

for i in range (0, 3):
    for j in range (0, 3):
        Lista.append(int(input(f"Digite o valor da posicao [{i + 1}, {j + 1}] da matriz: ")))
    Matriz.append(Lista[:])
    Lista.clear()

for i in range (0, 3):
    for j in range (0, 3):
        print(f"{Matriz[i][j]:^5}", end = '')
        if Matriz[i][j] % 2 == 0:
            SomaPares = SomaPares + Matriz [i][j]
        if j == 2:
            SomaColunas = SomaColunas + Matriz[i][j]
        if i == 1 and j == 0:
            Maior = Matriz[i][j]
        if i == 1:
            if Matriz[i][j] > Maior:
                Maior = Matriz[i][j]
    print()

print(f"A soma de numeros pares foi de {SomaPares}")
print(f"A soma dos numeros da terceira coluna eh {SomaColunas}")
print(f"O maior numero da segunda coluna da matriz eh {Maior}")
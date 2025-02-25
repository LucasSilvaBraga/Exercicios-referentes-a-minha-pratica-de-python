#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

#Matriz = [[] [] []]
#O indice da lista composta servira como linha e o indice da lista simples servira como coluna

Lista = []
Matriz = []
Linhas = 0
Colunas = 0

#Requisitando que o suario insira os dados da matriz
for i in range (0, 9):

    Lista.append(int(input(f"Digite o item [{Linhas + 1}, {Colunas + 1}]: ")))
    Colunas += 1
    if Colunas == 3:
        Linhas += 1
        Matriz.append(Lista[:])
        Lista.clear()
        Colunas = 0


#Formatando a exibicao
#(:) formatacao (^) centralizada (5) com 5 espacos
for i in range(0, 3):
    for j in range(0, 3):
        print(f"{Matriz[i][j]:^5}", end = '')
    print()



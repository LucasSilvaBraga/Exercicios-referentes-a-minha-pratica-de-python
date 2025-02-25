#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample

JogoIndividual = []
TodosJogos = []

NumeroJogos = int(input("Quantos jogos voce deseja que sejam gerados?: "))

#Solicitando o numero de jogos que o usuario deseja
#Utilizando o metodo sample da biblioteca random
#Os argumentos do metodo sample sao (intervalo em que o numero sera escolhido, quantos numeros serao escolhidos nesse intervalo)
for i in range (0, NumeroJogos):
    Lista = sample(range(1, 61), 6)
    print(Lista)
    TodosJogos.append(Lista[:])
    Lista.clear()

#Exibindo os jogos gerados
print("Os jogos gerados foram:")
for i in range (0, len(TodosJogos)):
    print(f"Jogo {i + 1}: ", end = '')
    for j in range (0, 6):
        print(f" {TodosJogos[i][j]}", end='')
        if j < 5:
            print(",", end = '')
    print()






#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

#importando a funcao randint  da biblioteca random que escolhe um valor inteiro dentro de um determinado intervalo
from random import randint

#Importando a funcao sleep da biblioteca time para dar um delay entre os comandos
from time import sleep

#Importando a funcao itemgetter da biblioteca operator para ordenar dicionarios
from operator import itemgetter

#Criando um dicionario e atribuindo um valor aleatorio a cada key
Jogo = {'Jogador 1' : randint(1, 6),
        'Jogador 2' : randint(1, 6),
        'Jogador 3' : randint(1, 6),
        'Jogador 4' : randint(1, 6)}

#Utilizar o metodo .item() em um dicionario fara com que seja retornadas suas respectivas keys e valores.
#Por isso atribuimos a esse retorno duas variaveis 'k' e 'v'.
#Utilizando a funcao for apenas com o retorno de 'Jogo.items()' o loop repetira de acordo com o tamanho de keys e items
print("Valores sorteados:")
for k, v in Jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(1)

#Ordenando o dicionario de acordo com os valores que foram sorteados

#Criando uma lista auxiliar
ranking = list()

#FUNCAO SORTED
#Argumento 1 --> o que sera ordenado? (No caso precisamos utilizar Jogo.items() para um dicionario para que sejam retornados valores e keys)
#Argumento 2 --> em funcao de que sera ordenado? (utilizando afuncao itemgetter para sinalizar que estamos utilizando os valores de cada key como referencia (nao poderia usar Jogo.values?))
#Argumento 3 --> Utilizando o comando reverse = True para inverter a ordem
ranking = sorted(Jogo.items(), key = itemgetter(1), reverse= True)

#Apos ordenarmos, o python trata o retorno da funcao sorted como um lista de tuplas, entao para exibi-la temos que trata-la de acordo

print(ranking)

#Exibindo os items em ordem
#A funcao enumerate retorna a posica da tupla dentro da lista e os dados dessa tupla v[0] para a posicao 0 da tupla e v[1] para a posicao 1 da tupla
print("Ranking:")
for i, v in enumerate(ranking):
    print(f"{i + 1} lugar: {v[0]} com {v[1]}")
    sleep(1)



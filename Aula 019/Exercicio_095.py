#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#Enunciado da questao 93. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

Dados = {}
Jogadores = []
Gols = []
FlagContinuar = ''
DicionarioAuxiliar = {}


while True:
    #Reiniciando a contagem de gols
    Soma = 0

    #Requisitando dados ao usuario
    Dados["Nome"] = str(input("Digite o nome do jogador: "))
    Dados["Partidas"] = int(input("Digite quantas partidas o jogador realizou: "))
    if Dados["Partidas"] > 0:
        for i in range(0, Dados["Partidas"]):
            Gols.append(int(input(f"Digite a quantidade de gols na partida {i + 1}: ")))
            Soma += Gols[i] 
    Dados["Gols por partida"] = Gols[:]
    Dados["Total de gols no campeonato"] = Soma

    #Atribuindo dados individuais a lista de jogadores
    Jogadores.append(Dados.copy())

    #Flag para continuar inserindo jogadores
    FlagContinuar = input("Deseja continuar digitando valores? (s/n): ").lower()
    while FlagContinuar != 'n' and FlagContinuar != 's':
        FlagContinuar = input("Digite uam resposta valida. Deseja continuar digitando valores? (s/n): ")
    if FlagContinuar == "s":
        break

#Exibicao de dados
i = 0
for i in range(0, len(Jogadores)):
    print(f"{i} ", end = '')
    DicionarioAuxiliar = Jogadores[i]
    for k, v in DicionarioAuxiliar.items():
        print(f"{DicionarioAuxiliar["Nome"]} --> {DicionarioAuxiliar["Gols por partida"]}")

 



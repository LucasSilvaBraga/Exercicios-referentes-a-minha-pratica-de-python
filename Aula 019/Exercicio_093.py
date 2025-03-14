#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

Dados = {}
ListaDeGols = []
Soma = 0

Dados["Nome"] = str(input("Digite o nome do jogador: "))
Dados["Partidas"] = int(input("Digite a quantidade de partidas que esse jogador ja realizou: "))
if Dados["Partidas"] > 0:
    for i in range (0, Dados["Partidas"]):
        ListaDeGols.append(int(input(f"Digite a quantidade de gols na partidada {i + 1}: ")))
        Soma += ListaDeGols[i]
    Dados["Gols em cada partida"] = ListaDeGols[:]
    Dados["Total de gols durante o campeonato"] = Soma
print("/n")

print("-=" * 30)
print(f"{"Dados do jogador":^55}")
for k, v in Dados.items():
    if k != "Gols em cada partida":
        print(f"{k}: {v}")
    else:
        print(f"{k}: ")
        for i in range (0, len(v)):
            print(f"Gols na partida[{i + 1}] --> {v[i]}")
print("-=" * 30)

    
#Na minha primeira hipotese sobre a copia de listas para outras estruturas havia a necessidade do uso do [:] para a atribuicao dessa lista a outra variiavel. Caso contrario ao invez de atribuirmos estariamos linkando a determinada variavel a aquela lista. De forma que se alterarmos a lista alteramos tambem o que esta dentro da referida variavel
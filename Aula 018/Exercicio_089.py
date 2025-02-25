#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

MatrizAlunos = []
DadosAlunoIndividual = []

while True:

    DadosAlunoIndividual.append(str(input("Digite o nome do aluno: ")))
    DadosAlunoIndividual.append(int(input("Digite a nota 1 do aluno: ")))
    DadosAlunoIndividual.append(int(input("Digite a nota 2 do aluno: ")))
    Media = (DadosAlunoIndividual[1] + DadosAlunoIndividual[2]) / 2
    DadosAlunoIndividual.append(Media)
    MatrizAlunos.append(DadosAlunoIndividual[:])
    DadosAlunoIndividual.clear()

    FlagContinuar = input("Deseja continuar cadastrando alunos? (s/n): ").lower()
    while FlagContinuar != 's' and FlagContinuar != 'n':
        FlagContinuar = input("Digite uma resposta valida: (s/n): ").lower()
    if FlagContinuar == 'n':
        break




print("-=" * 30)
print(f"{"BOLETIM":^55}")
for i in range (0, len(MatrizAlunos)):
    print(f"{MatrizAlunos[i][0]} -> Media {MatrizAlunos[i][3]}")
print("-=" * 30)




FlagConsulta = input("Deseja consultar as notas de cada aluno individualmente? (s/n): ").lower()
while FlagConsulta != 's' and FlagConsulta != 'n':
    input("Digite uma resposta valida. Deseja consultar as notas de cada aluno individualmente? (s/n): ").lower()
if FlagConsulta == 's':
    print("-=" * 30)
    print(f"{"BOLETIM":^55}")
    for i in range(0, len(MatrizAlunos)):
        print(f"{MatrizAlunos[i][0]}--> Nota 1: {MatrizAlunos[i][1]} | Nota 2: {MatrizAlunos[i][2]}")
    print("-=" * 30)


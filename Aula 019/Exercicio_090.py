#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

Aluno = {}
Alunos = []

while True:

    #Adicionando novas keys ao dicionario vazio 'aluno'
    Aluno["Nome"] = str(input("Digite o nome do aluno: "))
    Aluno["Media"] = float(input("Digite a media do aluno: "))

    #Utilizando o valor da media para definir a  nova key 'situacao'
    if Aluno["Media"] >= 7:
        Aluno["Situacao"] = "Aprovado"
    else:
        Aluno["Situacao"] = "Recuperacao"
        
    #Inserindo o dicionario que acabou de ser preenchido na lista 'alunos'. Dessa maneira cada aluno sera um dicionario, que sera inserido na lista.
    Alunos.append(Aluno.copy())

    #Flag para verificar se o usuario deseja ou nao continuar o programa
    FlagContinuar = input("Deseja continuar cadastrando alunos? (s/n): ").lower()
    if FlagContinuar != 's' and  FlagContinuar != 'n':
        FlagContinuar = input("Digite uma resposta valida. Deseja continuar cadastrando alunos? (s/n): ")
    if FlagContinuar == 'n':
        break

#Exibindo os dados inseridos
print("-=" * 30)
for i in Alunos:
    for k, v in i.items():
       print(f"{k}: {v}")
    print("-=" * 30)     



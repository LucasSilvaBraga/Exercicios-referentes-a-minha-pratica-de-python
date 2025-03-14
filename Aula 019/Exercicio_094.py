#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média


Dados = {}
PessoasCadastradas = []
DicionarioAuxiliar = {}
FlagContinuar = ''
Contador = 0
SomaIdades = 0


while True:

    Contador += 1

    #Cadastramento de pessoas
    Dados["Nome"] = str(input("Digite o nome da pessoa a ser cadastrada: "))
    Dados["Sexo"] = input("Digite o sexo da pessoa a ser cadastrado (m/f): ").lower()
    while Dados["Sexo"] != "f" and Dados["Sexo"] != "m":
        Dados["Sexo"] = input("Digite uma resposta valida. Digite o sexo da pessoa a ser cadastrado (m/f): ").lower()
    if Dados["Sexo"] == 'f':
        Dados["Sexo"] = 'Feminino'
    elif Dados["Sexo"] == 'm':
        Dados["Sexo"] = "Masculino"
    Dados["Idade"] = int(input("Digite a idade da pessoa a ser cadastrada: "))
    SomaIdades += Dados["Idade"]

    print(Dados)

    PessoasCadastradas.append(Dados.copy())


    #Verificacao para continuar inserindo pessoas
    FlagContinuar = input("Deseja continuar cadastrando pessoas? (s/n): ").lower()
    while FlagContinuar != 'n' and FlagContinuar != 's':
        FlagContinuar = input("Digite uma resposta valida. Deseja continuar cadastrando pessoas? (s/n): ").lower()
    if FlagContinuar == 'n':
        break
print("\n")

#Media das idades
MediaIdades = SomaIdades / Contador

print("-=" * 30)
print(f"{"MULHERES CADASTRADAS":^55}")
for i in range(0, len(PessoasCadastradas)):
    DicionarioAuxiliar = PessoasCadastradas[i]
    if DicionarioAuxiliar["Sexo"] == "Feminino":
        for k, v in DicionarioAuxiliar.items():
            print(f"{k}: {v}")
        print("-=" * 30)

print("\n")
print("-=" * 30)
print(f"{"PESSOAS ACIMA DA MEDIA DE IDADE":^55}")
print(f"A media das idades foi: {MediaIdades:.2f}")
for i in range (0, len(PessoasCadastradas)):
    DicionarioAuxiliar = PessoasCadastradas[i]
    if DicionarioAuxiliar["Idade"] > MediaIdades:
        for k, v in DicionarioAuxiliar.items():
            print(f"{k}: {v}")
        print("-=" * 30)    
    

#No gabarito eh uitilizado o metodo clear para limpar o dicionariiio antes de comecar o loop (ou seja a cada insercao de pessoa). Porem os comandos de input ja sobrescrevem a informacao passada do dicionario anterior. Logo a utilizacao do metodo .clear() nao parece necessaria.
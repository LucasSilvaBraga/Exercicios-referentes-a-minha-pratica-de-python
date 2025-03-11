#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#Considerando que para se aposentar e preciso ter 65 anos de idade + 20 anos de contribuicao

from datetime import datetime

Dados = {}


Dados["Nome"] = input("Digite o nome do trabalhador: ").strip()
Dados["Ano de nascimento"] = int(input("Digite o ano de nascimento do trabalhador: "))
Dados["Numero Carteira"] = int(input("Digite o numero da carteira de trabalho do trabalhador(digite 0 caso ainda nao esteja registrado): "))
if Dados["Numero Carteira"] != 0:
    Dados["Ano de contratacao"] = int(input("Digite o ano de contratacao do trabalhador: "))
    Dados["Salario"] = float(input("Digite o salario do trabalhador: "))

AnoAtual = datetime.now().year
TempoContribuicao = AnoAtual - Dados["Ano de contratacao"]
Idade = AnoAtual - Dados["Ano de nascimento"]

if TempoContribuicao >=  20 and Idade >= 65:
    print(f"{Dados['Nome']} ja esta elegivel para a aposentadoria")
elif TempoContribuicao >= 20 and Idade < 65:
    IdadeFaltante = 65 - Idade 
    print(f" O(A) sr.(sra) {Dados['Nome']} so estara elegivel para a aposentadoria em {IdadeFaltante} quando completar a idade minima de 65 anos")
elif TempoContribuicao < 20 and Idade > 65:
    TempoFaltante = TempoContribuicao - 20
    print(f"O(A) sr.(sra) {Dados['Nome']} so estara elegivel para a aposentadoria em {TempoFaltante} quando o tempo minimo de contribuicao de 20 anos for completo")
elif TempoContribuicao < 20 and Idade > 65:
    

print(Dados)



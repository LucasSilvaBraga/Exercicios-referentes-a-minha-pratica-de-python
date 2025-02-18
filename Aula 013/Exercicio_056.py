#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A media de idade do Grupo
#Qual e o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos 

Media = 0 
Nome = ''
Genero = ''
MaiorHomem = 0
MenorQue20 = 0

for i in range(0, 4):
    Nome = str(input("Digite o nome da pessoa [{}]: ". format(i + 1)))
    Genero = (input("Digite o genero da pessoa (M/F)[{}]". format(i + 1))).upper()
    Idade = int(input("Digite a idade da pessoa [{}]: ". format(i + 1)))

    

    if Genero == 'M':
        if Idade > MaiorHomem:
            MaiorHomem = Idade
            NomeMaior = Nome
    
    if Genero == "F":
        if Idade < 20:
            MenorQue20 += 1

    Media += Idade



Media = Media / 4
print("=-=-=-=-=DADOS=-=-=-=-=\nO homem mais velho do grupo: {}\nIdade: {} anos\n\nQuantidade de mulheres com menos de 20 anos: {}". format(NomeMaior.upper(), MaiorHomem, MenorQue20))
print("\nMedia de idade do grupo: {}". format(Media))


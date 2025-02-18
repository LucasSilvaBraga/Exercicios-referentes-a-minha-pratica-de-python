#Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoas cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. No final mostre:
#Quantas pessoas tem mais de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 anos

Contador = 1
ContadorIdade = 0
ContadorMasculino = 0
ContadorFeminino = 0

while True:
    Idade = int(input(f"Digite a idade da pessoa [{Contador}]: "))

    Genero = input(f"Digite o genero da pessoa [{Contador}] (F/M): ").upper()
    while Genero != 'F' and Genero != 'M':
        Genero = input(f"Digite o genero da pessoa [{Contador}] (F/M): ").upper()

    if Idade > 18:
        ContadorIdade += 1
    if Genero == 'M':
        ContadorMasculino
    if Genero == 'F' and Idade < 20:
        ContadorFeminino

    Resposta = str(input("Quer continuar a cadastrar pessoas(sim/nao)? ")).upper()
    if Resposta == 'NAO':
        print(f"Total de pessoas com mais de 18 anos: {ContadorIdade}")
        print(f"Total de homens cadastrados: {ContadorMasculino}")
        print(f"Total de mulheres com menos de 20 anos cadastradas: {ContadorFeminino}")
        break

    Contador += 1

#A confederacao Nacional de natacao precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria de acordo com a idade
#Ate 9 anos: Mirim
#Ate 14 anos: infantil
#Ate 19 anos: Junior
#Ate 25 anos: Senior
#Acima: Master

Idade = int(input("Digite sua idade: "))

if Idade <= 9:
    print("Voce eh uma atleta Mirim")
elif Idade > 9 and Idade <= 14:
    print("Voce eh um atleta infantil")
elif Idade > 14 and Idade <= 19:
    print("Voce eh um atleta Junior")
elif Idade > 19 and Idade <= 25:
    print("Voce eh um atleta senior")
else:
    print("Voce eh um atleta master")

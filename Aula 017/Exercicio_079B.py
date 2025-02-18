#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

#Gabarito do video

#Iniciando uma lista vazia
Numero = list()

#Fazendo um loop infinito
while True:
    n = int(input("Digite um valor: "))
    
    #Utilizando os operadores 'not' e 'in' para verificar se o numero amazenado na variavel n nao esta na lista 'Numero'
    if n not in Numero:
        Numero.append(n)
        print("Valor adicionado com sucesso")
    else: 
        print("Valor duplicado, nao vou adicionar")

    #Requisitando ao usuario se ele deseja ocntinuar ou nao
    r = str(input("Quer continuar (s/n): "))

    #Utilizando o operador in para verificar se a resposta armazenada na variavel r eh 'n' ou 'N'
    if r in 'Nn':
        break

print('-=' * 30)
Numero.sort()
print(f"Voce digitou os valores {Numero}")



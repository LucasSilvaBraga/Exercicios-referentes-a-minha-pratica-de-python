#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

#Gabarito do video

Valores = []

while True:
    Valores.append(int(input('Digite um valor: ')))

    #Requisitando ao usuario se ele deseja parar de digitar valores
    Resp = str(input("Quer continuar? (s/n): "))
    if Resp in 'Nn':
        break

print('-=' * 30)

#Mostrando a quantidade de elementos na lista
print(f"Voce digitou {len(Valores)} elementos.")

#Mostrando os valores em ordem decrescente
#Utilizando o metodo sort com o parametro 'reverse = true' para ordenar a lista de maneira decrescente
Valores.sort(reverse = True)
print(f"A lista em ordem decrescente eh: {Valores}")

#Utilizando o operador in para verificar se o 5 esta dentro da lista
if 5 in Valores:
    print("O valor 5 esta na lista!")
else:
    print("O valor 5 nao esta na lista!")


#Faca um programa que leia 5 valores numericos e guarde-os em uma lista
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posicoes na lista

#Lista = []
#Maior = 0
#Menor = 9999999999

#for i in range (0, 5):
    #Lista.append(int(input(f"Digite o valor [{i + 1}]: ")))
    #if Lista[i] > Maior:
        #Maior = Lista[i]

#print(f"Sua lista foi: {Lista}\nO maior valor digitado foi: {Maior}")

#=-=-=-=-= GABARITO (mais elegante) =-=-=-=-=
Lista = []
Maior = 0
Menor = 0

for c in range(0, 5):
    Lista.append(int(input(f"Digite o valor [{c + 1}]: ")))
    if c == 0:
        Maior = Menor = Lista[c]
    elif Lista[c] > Maior:
        Maior = Lista[c]
    elif Lista[c] < Menor:
        Menor = Lista[c]
        
print(f"Sua lista eh: {Lista}\nO maior numero eh: {Maior}\nO menor numero eh: {Menor}")

#=-=-=-=-= SOLUCAO INCORRETA =-=-=-=-=-
#Fazer como em linguagem c, mesmo em linguagem c ainda precisamos determinar o tamanho da lista

#for i in range (0, 5):
#    Lista[i] = int(input(f"Digite o valor [{i + 1}]: "))




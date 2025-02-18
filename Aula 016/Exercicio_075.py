#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre
#A) Quantas vezes apareceu o valor 9
#B) Em que posicao foi digitado o valor 3
#C) Quais os numeros pares

#=-=-=-=-=-Solucao 1=-=-=-=-=-

#Como isso esta funcionando?
#Est no formato de list comprehension porem no liist comprehension a variada gerada pela estrutura for - que no caso atual se trata da variavel 'c' - era retornada para o lado esquerdo da expressao o que nao acontece nesse caso

#Valores = tuple(int(input('Digite valores ')) for c in range(0, 5))

#Contagem = 0
#ValoresPares = []


#for i in range (0, 5):
#    if Valores[i] == 9:
#        Contagem += 1
#    if Valores[i] == 3:
#        PosicaoTres = i
#    if Valores[i] % 2 == 0:
#        ValoresPares.append(Valores[i])


    


#print(f"A quantidade de vezes que o valor 9 aparece eh: {Contagem}")

#print(f"A posicao do numero 3 eh: {PosicaoTres + 1}")

#print(f"Os numeros pares dessa tupla sao: ", end = '')
#for i in range (0, len(ValoresPares)):
#    print(f"{ValoresPares[i]}, ", end = '')


#=-=-=-==-Solucao do gabarito=-=-=-=-=-=-



Valores = (int(input("Digite um valor: ")), int(input("Digite outro valor: ")), int(input("Digite mais um outro valor: ")), int(input("Digite o ultimo valor: ")))

print(f"A quantidade de vezes que o valor 9 apareceu foi: {Valores.count(9)}")\
#Cuidado!!! utilizando o index, caso o numero 3 nao esteja presente na sequencia, o programa vai bugar, por isso temos que inserir um condicional
if 3 in Valores:
    print(f"O numero tres esta na {Valores.index(3) + 1}° posicao")
else:
    print("O valor 3 nao foi digitado em nenhuma posicao")
print("Os valores pares digitados foram:")
for i in range (0, 4):
    if Valores[i] % 2 == 0:
        print(f"{Valores[i]} ", end = '')



    

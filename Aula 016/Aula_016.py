#-----TUPLAS-----

#eh um vetor de linguagem C
#Para isso usamos parenteses (tambem e possivel fazer sem)

Lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata frita")
print(f"Mostrando o 4 elemento da lista: {Lanche[3]}")

#A lista tambem pode ser vista de maneira invertida
print(f"A lista tambem pode ser vista de maneira iinvertiida: {Lanche[-2]}")

#Podemos fazer o fatiamento mostrando uma serie de elementos
print(f"Fatiamento de elementos: {Lanche[0:3]}")

#Fazendo de determinado elemento ate o final
print(f"De um determinado elemento ate o final: {Lanche[-2:]}")

#Fazendo do comeco ate o final
print(f" Fazendo do comeco ate o final {Lanche[:]}")

#Tuplas sao imutaveis, elementos so podem ser atribuidos em sua declaracao e nada mais que isso
#Lanche[1] =  "Refrigerante"

#Ha uma maneira de exibir a tupla no laco for sem precisar de um contador
print("Exibindo a tupla sem precisar de uma variavel contadora")
for i in Lanche:
    print(f"Eu vou comer: {i}")

#Agora utilizando uma variavel contadora ou seja da maneira convencional
print("Agora utilizando uma variavel contadora ou seja da maneira convencional")
for i in range(0 ,len(Lanche)):
    print(f"vou comer {Lanche[i]}")

#Utilizando loops de repetiicao ha uma maneira de saber a posicao de cada elemento na tupla
#A funcao enumerate vai atribuir a posicao correspondente atual na primeira variavel definida antes do in
print("For sabendo a posicao de cada elemento da tupla")
for Pos, Comida in enumerate (Lanche):
    print(f"Eu vou comer {Comida} na posicao {Pos}")

#Existe um comando que exiibe a tupla em ordem diferente (perceba que a tupla nao foi alterada apenas foi exibida em uma ordem diferente)
print(sorted(Lanche))

#Somando tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(f"Tupla a: {a}")
print(f"Tupla b: {b}")
print(f"Tupla b + c:  {c}")

#Contando quantas ocorrencias de um elemento
print(f"Contando quantas ocorrencias de um elemento: {c.count(5)}")

#Achando a posicao de determinado elemento numa lista
print("Mostrando a posicao de determinado objeto em uma tupla (No caso de Hamburguer): ", end = '')
print(Lanche.index("Hamburguer"))

#Tuplas tambem possuem a funcao min e max que indicam qual e o menor e maior numero
print(f"O menor numero eh: {min(c)}")
print(f"O maor numero eh: {max(c)}")

#-=-=-=-=-=- LIST COMPREHENSIION -=-=-=-=-=-

#Ver depois sobre list comprehension







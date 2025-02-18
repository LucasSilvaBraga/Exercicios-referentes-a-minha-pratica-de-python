#FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.
#EX: Ana Maria de Souza 
#Primerio = Ana
#Último = Souza

Nome = str(input("Digite seu nome: "))



print(Nome[0:Nome.find(' ')])

print(Nome[Nome.rfind(' '):])

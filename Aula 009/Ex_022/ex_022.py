#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
#NOME COM TODAS AS LETRAS MAIUSCULAS
#NOME COM TODAS AS LETRAS MINUSCULAS 
#QUANTAS LETRAS AO TOdO (SEM CONTAR OS ESPAÇOS)
#QUANTAS LETRAS TEM O PRIMEIRO NOME 

Nome = input("Digite um nome: ")

#Transformando todas as letras em maiusculas
print("\n{}". format(Nome.upper()))
#Nome com todas as letras minusculas
print("\n{}". format(Nome.lower()))
#Quantidade de caracteres sem espacos 
QuantidadeDeEspacos = Nome.count(' ')
QuantidadeDeCaracteres = len(Nome)
print('\n{} tem {} letras sem contar os espacos\n'. format(Nome, (QuantidadeDeCaracteres - QuantidadeDeEspacos)))

#OBS: perceba que Nome.upper(), Nome.lower(), Nome.count(' '), sao metodos que utilizam "Nome" como objeto, sendo que apenas count(' ')
#possui um argumento, ambas nao alteram a variavel original, ou seja, possuem um retorno

#Mostrando a quantidade de letras do primerio nome
PrimeiroNome = Nome.split()
PrimeiroNome = len(PrimeiroNome[0])
print("A quantidade de letras do primeiro nome eh: {}". format(PrimeiroNome))

#Lembrando que o metodo .split divide a string em varias outras strings, nesse caso o parametro de divisao esta sendo o caractere de espaco
#E criada um matriz em que cada divisao eh representada por um numero no inicio da coluna e o resto da linha e a string (mais ou menos isso....) 

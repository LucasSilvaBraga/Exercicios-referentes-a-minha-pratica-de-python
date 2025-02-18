#====Faca um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor ====

#em python nao precisamos declarar variaveis, apenas escreve-las ja eh suficiente
#As leituras a partir do teclado sao feitas pelo comando 'input'
#Para o python todos o carcteres lidos atraves do input sao strings por isso e preciso transformar os caracteres lidos no tipo de variavel desejada com 'int()'
n1 = int(input('Digite um numero: '))

#Para inserir uma informacao vinda de uma variavel e preciso utilizar '{}' para se referir aonde a informacao sera inserida e utilizar '.format("variavel_em_questao")'
print('O antecessor do seu numero eh: {}'. format(n1 - 1))
print('O sucessor do seu numero eh: {}'. format(n1 + 1))

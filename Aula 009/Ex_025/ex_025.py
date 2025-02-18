#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E DIGA SE ELA TEM SILVA NO NOME 

Nome = str(input("Digite o seu nome: "))
Nome = Nome.lower()
#O operador 'in' verifica se essa sequebncia de letras existe dentro da string, caso exista exibira 'True'
print('silva' in Nome) 



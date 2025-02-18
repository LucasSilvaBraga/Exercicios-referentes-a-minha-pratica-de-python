#FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#QUANTAS VEZES APARECE A LETRA R
#EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ 
#EM QUE OPÇÃO ELA APARECE POR ULTIMO

Nome =  str(input("Digite uma frase: "))
Nome = Nome.lower()

print('A letra r aparece {} vezes'.format(Nome.count('r')))

print("A primeira aparicao da letra r e na posicao {}".format(Nome.find('r')))

#Colocando r no metodo "find" sera encontrado apenas o argumento desejado mais a direita
print("A ultima aparicao da letra r e na posicao {}".format(Nome.rfind('r')))


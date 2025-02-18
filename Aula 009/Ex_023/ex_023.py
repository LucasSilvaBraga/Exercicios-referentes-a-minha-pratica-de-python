#FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS
#EX:
#DIGITE UM NUMERO:1834
#UNIDADE:4
#DEZENA:3
#CENTENA:8
#MILHAR:1

Numero = int(input('Digite um numero: '))

print("Unidade: {}". format(Numero // 1))
print("Dezena: {}". format(Numero // 10)) 
print("Centena: {}". format(Numero // 100)) 
print("Milhar: {}". format(Numero // 1000)) 
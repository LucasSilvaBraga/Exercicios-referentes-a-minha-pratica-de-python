#Faca um programa que leia um numero qualquer e mostre o seu fatorial

Numero = int(input("Digite um numero qualquer e o programa mostrara o seu fatorial: "))

NumeroRequisitado = Numero
Contador = Numero

while Contador > 1:
    Contador -= 1
    Numero = Numero * Contador 

print("O fatorial de {} eh: {}". format(NumeroRequisitado, Numero))


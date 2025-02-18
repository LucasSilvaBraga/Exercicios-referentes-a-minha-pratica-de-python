#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
# Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso

#Obs: Vai ler ate 5 pois nao achei necessario digitar os outros
NumerosExtensos = ("Zero", "Um", "dois", "Tres", "Quatro", "Cinco")

NumerosNormais = int(input("Digite um numero: "))
print(f"Voce digitou {NumerosExtensos[NumerosNormais]}")


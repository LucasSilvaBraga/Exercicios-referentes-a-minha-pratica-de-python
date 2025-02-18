#FAÇA UM PROGRAMA QUE LEIA TRES NUMEROS E MOSTRE QUAL É O MAIOR E QUAL É O MENOR

Numero1 = float(input("Digite o primeiro numero: "))
Numero2 = float(input("Digite o segundo numero: "))
Numero3 = float(input("Digite o terceiro numero: "))

if Numero1 > Numero2 and Numero1 > Numero3:
    print("Maior numero: {}". format(Numero1))
    if Numero2 > Numero3:
        print("Menor Numero: {}". format(Numero3))
    else:
        print("Menor Numero: {}". format(Numero2))

if Numero2 > Numero1 and Numero2 > Numero3:
    print("Maior numero: {}". format(Numero2))
    if Numero1 > Numero3:
        print("Menor numero: {}". format(Numero3))
    else:
        print("Menor Numero: {}". format(Numero1))

if Numero3 > Numero1 and Numero3 > Numero2:
    print("Maior numero: {}". format(Numero3))
    if Numero2 > Numero1:
        print("Menor numero: {}". format(Numero1))
    else:
        print("Menor numero: {}". format(Numero2))
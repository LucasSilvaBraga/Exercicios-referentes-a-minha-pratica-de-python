#Crie um programa que tenha uma tupla com várias palavras (nao usar acentos). Depois disso, voce deve mostar, para cada palavra, quais sao suas vogais.

Palavras = ("Laranja", "Limao", "Sorvete", "Abacaxi", "Cadeira", "Morango", "Cachorro")


for i in range(0, len(Palavras)):
    print(f"As vogais da palavra {Palavras[i]} sao: ", end = '')
    for j in range (0, len(Palavras[i])):
        if 'a' ==  Palavras[i][j]:
            print(f"{Palavras[i][j]} ", end = '')
        if "e" == Palavras[i][j]:
            print(f"{Palavras[i][j] } ", end = '')
        if 'i' ==  Palavras[i][j]:
            print(f"{Palavras[i][j]} ", end = '')
        if "o" == Palavras[i][j]:
            print(f"{Palavras[i][j] } ", end = '')
        if 'u' ==  Palavras[i][j]:
            print(f"{Palavras[i][j]} ", end = '')
        
    print("\n")






#Crie um programa que leia uma frase qualquer e diga se ela eh um palindromo, desconsiderando os espacos

#Utilizando strip e upper para tirar possiveis espacos da esquerda e da direita e deixando todas as letras maiusculas
Frase = str(input("Digite uma frase: ")).strip().upper()

#tirando os possiveis espacos entre as palavras da frase
Separado = Frase.split()
Junto = ''.join(Separado)

#Invertendo a frase utilizando uma estrutura de repeticao for
# Como vamos inverter a frase temos que comecar do final dela, para isso utilizaremos a funcao 'len()', que diz o numero de letras em uma frase.
# Porem mesmo que o tamanho esteja correto a string vai ate 'NumeroDeLetras - 1', para verificar isso basta lembrar que a strings sempre comecam em 0.
# O loop ira parar quando i < -1 para que cubra a string por inteiro e com o passo de -1 (i--). 

#Funcionamento dentro do for
# Temos que lembrar que uma string nada mais eh do que um vetor de char, por isso, cada letra ja esta separada em sua devida posicao com o tamanho do vetor sendo len(Junto) '-1'
# Sendo assim, iremos adicionar letra por letra de maneira inversa (gracas a logica do for) a um outro vetor de char criado previamente chamado 'Inverso',
# o mesmo esta igualado a '; que indica que ele eh um vetor vazio
Inverso = ''
for i in range(len(Junto) -1, -1, -1):
    Inverso += Junto[i]

if Inverso == Junto:
    print("{} e {} sao palindromos". format(Inverso, Junto))
else:
    print("{} e {} nao sao palindromos". format(Inverso, Junto))






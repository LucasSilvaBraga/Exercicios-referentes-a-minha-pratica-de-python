#O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA

import random

Alunos = ['Andre', 'Bianca', 'Carlos', 'Daniela']
random.shuffle(Alunos)
print('A ordem de apresentacao sera: {}'. format(Alunos))

#OBS: nao e possivel utilizar: print('A ordem de apresentacao sera: {}'. format(math.shuffle(Alunos)))
#Provavelmente porque a funcao shuffle ja executa o embaralhamente e tambem ja SALVA a nova ordem nos seus atributos, ou seja, ela nao tem retorno
#(talvez seja feita por enderecamento) 

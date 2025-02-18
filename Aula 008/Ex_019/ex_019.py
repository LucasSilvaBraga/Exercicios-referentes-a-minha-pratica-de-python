#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO, FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME ESCOLHIDO

import random
#Criando um vetopr de alunos
Alunos = ['Andre', 'Bianca', 'Carlos', 'Daniela']
print("Os alunos sao: {}". format(Alunos))

Escolha = random.choice(Alunos)
print("O aluno escohido para apagar o quadro foi: {}". format(Escolha))

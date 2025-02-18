#====MANIPULANDO TEXTO====


frase = 'Curso em Video Python'
frase1 = '   curso em video python   '

#Mostrando apenas a letras na posição lembrando que strings são contadas em: 0  1  2  3  4  5  6  7  8  9  10 (começando do zero)
print('mostando apenas a letra na posição 9: {}'. format(frase[9]))

#Mostrando letras utilizando um range, observe que a letra na posição 13 não é utilizada (ou seja so vai de 9 a 12)
print('mostrando a letra da pocição 9 ate 13: {}'. format(frase[9:13]))

#Mostrando de *vídeo* até o final (repare que essa string possui 20 caracteres, entao colocamos 21 como o final do range para que a ultima letra nao seja apagada)
print('mostrando de *video* ate o final: {}'. format(frase[9:21])) 

#Mostrando as letras de 9 até o final pulando de dois em dois espaços
print('Mostrando as letras de 9 até o final pulando de 2 em 2: {}'. format(frase[9:21:2]))

#Mostrando de 0 (por padrão) até o slot 5
print('Mostrando de 0 (por padrão) até o slot 5: {}'. format(frase[:5]))

#Mostrando de 15 ate o final (por padrão)
print('Mostrando de 15 ate o final (por padrão): {}'. format(frase[15:]))

#Mostrando em um range de 9 ate o final (por padrão) pulando de 3 em 3 
print('Mostrando em um range de 9 ate o final (por padrão) pulando de 3 em 3: {}'. format(frase[9::3]))

#Mostrando o comprimento de uma string
print('O tamanho da string é:', format(len(frase)))

#Contando apenas o numero de letras determinadas por mim na frase
print('o numero de letras *o* na frase é:', format(frase.count('o'))) 

#Contando apenas o numero de letras determinadas por mim na frase com fatiamento 
print('o numero de letras *o* na frase do slot 0 ao 13: ', format(frase.count('o', 0, 13)))

#Achando aonde começa uma determinada sequencia de letras 
print ('Achando aonde começa a sequencia de letras *deo*: ', format(frase.find('deo')))

#Caso a sequencia de letras dejada não exista o terminal vai retornar o valor -1 
print('Tentando procurar uma sequencia de letras que nao existe: ', format(frase.find('Android')))

#Verificando se uma sequencia de letras existe ou não na frase 
print('Verficando se o conjunto de letras *curso* existe na palavra python: ', format('Curso' in frase))

#Substituindo uma palavra por outra
print('Subistitundo palavras, no caso python para android: {}'. format(frase.replace('Python', 'Android')))

#Transformando tudo em maiúsculo
print('Substituindo para maiusculo: {}'. format(frase.upper()))

#Transformando tudo em minúsculo
print('Transformando todos os caracteres para minusculo: {}'. format(frase.lower()))

#Transforma toda a string para minusculo exceto o primeiro cacractere
print('Transformando todos os caracteres para minusculo exceto o primeiro: {}'. format(frase.capitalize()))

#Transformando sua string em titulo (ou seja a cada espaço a proxima letra será transformada em maiusculo)
print('Transformando a string em um título: {}'. format(frase.title()))

#Removendo espaços a frente ou atras que nao servem para nada
print('Removendo espaços a frente ou atras que nao servem para nada: {}'. format(frase1.strip()))

#Removendo somente os espaços as direita
print('Removendo somente os espaços a direita: {}'. format(frase1.rstrip()))

#Removendo somente os espaços as esquerda
print('Removendo somente os espaços a esquerda: {}'. format(frase1.lstrip()))

#separando cada palavra em uma string diferente (cada espaço serve como caractere divisor. Faz uma matriz em que cada coluna vira o numero daquela palavra *começando em 0* e as linhas sao os caracteres)
print('Dividindo um string em uma lista: {}'. format(frase.split()))

#Juntando uma frase ja separada por espaço com o carctere desejado no meio no caso o '-'
print('Juntando uma frase ja separada por espaços com um caractere qualquer, nesse caso o *-*: {}'. format('-'.join(frase))) 

#====FUNÇÕES QUE FORAM UTILIZADAS====
#[9] --> Ao final de uma variavel guardando uma string para indicar a letra na determinada posição (no caso 9)
#[9:13] -->Mostra os caracteres de 9 ate 12 (nao mostrando a posição 13)
#[9:21:2] --> Mostra os caracteres de 9 ate 21 pulando de 2 em 2
#[:5] --> Mostrando de 0 (por padrão) até o slot 5
#[15:] --> Mostrando de 15 ate o final (por padrão)
#[9::3] --> Mostrando em um range de 9 ate o final (por padrão) pulando de 3 em 3 
#len(frase) --> Mostrando o comprimento de uma string
#frase.count('o') --> Contando apenas o numero de letras determinadas por mim na frase (pode ser uma variavel em 'o' também)
#frase.count('o', 0, 13) --> Contando apenas o numero de letras determinadas por mim na frase com fatiamento
#frase.find('deo') --> Achando aonde começa uma determinada sequencia de letras 
#frase.replace('palavra que eu procuro' 'Palavra será colocada no lugar') --> substitui uma serie de caracteres por outra serie de caracteres
#frase.upper() --> Deixa todos os caracteres da string em maiusculo
#frase.lower() -->
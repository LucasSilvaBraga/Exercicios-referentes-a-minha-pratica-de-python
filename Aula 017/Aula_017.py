#Se as tuplas eram imutaveis as listas sao mutaveis
#Como em C, temos que pelo menos definir o tamanho da lista que gostariamos de criar
Num = [2, 5, 9, 1]
print(f"Lista antes da modificacao: {Num}")
Num[2] = 3
print(f"Lista apos a modificacao: {Num}")

#METODO .APPEND
print("METODO APPEND")
#Utilizando o metodo .append adicionamos o elemento contido no argumento na ultima posicao da lista, ou seja, uma nova posicao eh criada
#Caso tentemos adicionar um novo elemento a uma nova posicao 'Num[4] = 7' o codigo nao rodara 
Num = [2, 5, 9, 1]
print(f"Lista antes de adicionarmos um novo elemento: {Num}")
Num.append(7)
print(f"Lista apos adicionarmos um novo elemento: {Num}")
print("\n")

#METODOS DE ORDENACAO
print("METODOS DE ORDENACAO")
#Ordenando esses elementos em ordem crescente com o metodo .sort()
print(f"Ordenando esses elementos em ordem crescente: {Num}")

#Ordenando esses elementos em ordem reversa com o argumento 'reverse = True'
#Repare que nos dois ultimos exemplos a lista 'Num' foi alterada, o que nao aconteceria caso estivessemos usando tuplas
Num.sort(reverse = True)
print(f"Ordenando esses elementos de maneira decrescente{Num}")
print("\n")

#METODO INSERT
print("METODO INSERT")
#Utilizando o metodo .insert, podemos inserir elementos em qualquer posicao da lista que desejarmos. Se a lista possui tamanho 4 e desejarmos inserir um elemento na posicao 2 o segundo elemento original sera jogado para tras e o novo elemento ocupara a posicao desse, no final essa lista tera tamanho 5
#Os argumentos da funcao insert sao .insert(Na posicao x, insira o elemento y).
#Se a lista tiver tamanho 4 e quisermos inserir um elemento na posicao 6 o meotodo .insert vai apenas adicionar o novo elemento na ultima posicao disponivel e, no caso, a lista ficara com tamanho 5
print(f"Lista atual: {Num}")
Num.insert(2, 0)
print(f"Lista apos ser utilizado o metodo .insert inserindo o numero 0 na segunda posicao: {Num}")
print("\n")

#METODO POP
print("METODO POP")
#Utilizando o metodo .pop para remover um elemento da lista de acordo com sua posicao
#Caso o metodo seja utilizado sem nenhum argumento o ultimo elemento da lista sera removido
#Utilizando um argumento no metodo .pop podemos especificar em qual posicao um elemento deve ser removido. No caso o elemento que esta na posicao a frente toma a posicao do que foi removido
print(f"Lista atual: {Num}")
Num.pop()
print(f"Lista apos utilizar o metodo .pop sem argumentos: {Num}")
Num.pop(2)
print(f"Lista apos utilizar o metodo pop com o argumento (2): {Num}")
print("\n")


#METODO REMOVE
print("METODO REMOVE")
#O metodo .remove(), diferente do .pop(), remover um elemento de acordo com ele mesmo e nao de acordo com sua posicao
print(f"Lista atual: {Num}")
Num.remove(7)
print(f"Lista apos o .remove(7): {Num}")
#Caso tenhamos 2 elementos iguais numa mesma lista e utilizarmos .remove para remove-lo o metodo ira remover apenas o primeiro deles
Num.insert(0, 2)
print(f"Adicionando mais um elemento '2' a lista: {Num}")
Num.remove(2)
print(f"Utilizando remove com o argumento '2': {Num}")
#Caso tentemos remover um valor que nao esta na lista o metodo apresentara um erro para isso faremos um controle utilizando condicionais
print("Tentando utilizar .remove com um elemento que nao existe no caso '4' ")
if 4 in Num:
    Num.remove(4)
else:
    print("O numero 4 nao foi encontrado")
    
print("\n")

#FUNCAO ENUMERATE
#retorna a posicao de cada elemento em uma lista ou tupla
frutas = []

frutas.append("Maca")
frutas.append("Banana")
frutas.append("Uva")

#O primeiro argumento do for sera o retorno da funcao enumerate e o segundo argumento do for sera a propria lista enumerada.
#E como um for com dois argumentos (ver list comprehension)
#Ou seja, fruta, vai sempre assumir um valor em frutas entao o argumento de enumerate esta sempre alternando, e essa funcao retornara a posicao atual de 'fruta' a cada loop do for
for i, fruta in enumerate(frutas):
    print(i, fruta)
print("\n")


#UTILIZANDO A FUNCAO APPEND PARA INSERIR VALORES EM UMA LISTA
#Lista1 = []
#for i in range (0, 3):
#    Lista1.append(int(input(f"Digite o valor[{i+1}]: ")))

#print(f"Os valores digitados foram:{Lista1}")

#ATENCAO: NEM SEMPRE E POSSIVEL COPIAR UMA LISTA NO PYTHON
print("Linkando as listas")
A = [2, 3, 4, 7]
B = A
B[2] = 8
print(f"Lista A: {A}\nLista B:{B}")
#Repare que a alteracao de B nao deveria afetar A, mas afetou, isso se deve ao fato de que o python nao copia uma lista em outra e sim cria um LINK entre as duas, dessa maneira tudo que for mudado em uma altera a outra e vice versa
#A maneira correta de copiar uma lista na outra eh utilizando fatiamento:
print("Copiando uma lista na outra atravez de fatiamento")
A = [2, 3, 4, 7]
B = A[:]
B[2] = 8
print(f"Lista A: {A}\nLista B:{B}")

#Obs: repare que utilizando um metodo nos nunca precisamos retornar a atualizacao a uma variavel. 

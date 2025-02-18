#Uma maneira mais rapida e mais limpa de se escrever um estrutura de lista
#=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
#Exercicio 1: dobre o valor dos produtos da lista

#FAZENDO NORMALMENTE

ListaPrecos = [500, 1500, 2000, 100, 25]
print("O preco de cada produto da lista eh:")
print(ListaPrecos)

NovaListaPrecos = []

for Preco in ListaPrecos:
    #Utilizando .append para adicionar novos valores a lista (so adiciona novos valores nao substitui os antigos)
    NovaListaPrecos.append(Preco * 2)

#POR LIST COMPREHENSION

#'for preco in ListaPecos' ira retornar o item atual da lista(cada vez um item diferente), no caso ira retornar 'preco' em seguida preco sera multiplicado por 2 em 'preco * 2' e sera retornado para NovaListaPrecos2
#Repare que 'NovaListaPrecos' nao precisou ser iniciada no inicio apenas igualamos ela a uma expressao, repare tambem que essa expressao esta ente colchetes demonstrando que o que sair daquela expressao sera retornado em forma de lista
NovaListaPrecos2 = [Preco * 2 for Preco in ListaPrecos]

print("Nova lista de precos 2:")
print(NovaListaPrecos2)

#=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=
#Exercicio 2: Todos os itens que estiverem acima de 1000 dolares terao imposto de 50% sobre o valor total

#FAZENDO DE MANEIRA COMUM
Imposto = []

for Preco in ListaPrecos:
    if Preco > 1000:
        Imposto.append(Preco * 1.5)
    else:
        Imposto.append(Preco)

print("A lista de produtos com imposto de importacao eh:")
print(Imposto)

#FAZENDO POR LIST COMPREHENSION

#Nesse caso eh colocada depois 
#Porem (ate onde eu sei) so poderao ser retornados os valores com que cairem dentro do iif, ou seja valores a baixo de 1000 dolares nao serao retornados, ja que o list comprehension eh utilizado apenas para casos simples
Imposto2 = [Preco * 1.5 for Preco in ListaPrecos if Preco > 1000 ]

print("A lista com impostos2 eh:")
print(Imposto2)















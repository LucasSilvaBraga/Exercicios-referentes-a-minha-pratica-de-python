#Sobre o funcionamento do link na atribuicao de listas a outras estruturas
#Spoiler: sempre utilize o fatiamento para adicionar um lista a outra estutura

#Quando desejamos fazer listas compostas apenas atribuimos uma lista a outra como no exemplo abaixo
Lista1 = []
Lista2 = []

Lista1.append("Gustavo")
Lista1.append(40)

Lista2.append(Lista1)
print(Lista1)
print(Lista2)

Lista1.append(50)

#Porem quando simplesmente atribuimos uma a outra a lista simples, inicialmente criada, nao e copiada para a lista simples dentro da lista composta e sim fica likada com a liista simples de fora da lista composta.
#Dessa maneira qualquer alteracao feita na lista simples de fora alterara a lista simples de dentro
print("A lista simples esta linkada a outra lista simples que agora pertence a lista composta: ")
print(Lista1)
print(Lista2)
print("\n")

#Para evitar isso deve-se usar a tecnica do fatiamento durante a atribuicao de uma lista a outra. Vamos refazer o codigo dessa vez com fatiamento.
Lista3 = []
Lista4 = []

Lista3.append("Gustavo")
Lista3.append(40)

Lista4.append(Lista3[:])
print("Criando outras duas novas listas")
print(Lista3)
print(Lista4)

Lista3.append(50)
#Perceba que agora a lista simples de fora nao esta mais linkada com a lista simples de dentro
print("Perceba que agora a lista simples de fora nao esta mais linkada com a liista simples de dentro")
print(Lista3)
print(Lista4)







#Esse fenomeno tambem ocorre quando estamos atribuindo uma lista simples a um dicionario
print("-=" * 30)
Dados1 = {}
ListaDeGols1 = [1, 2 ,3]
Dados1["Gols"] = ListaDeGols1

print("Antes de atribuir um novo valor a lista simples fora do dicionario")
print(Dados1["Gols"])

print("Depois de atribuir um novo valor a lista simples dentro do dicionario")
ListaDeGols1.append(9)
print(Dados1["Gols"])

#Para resolver isso basta atribuir com a tecnica do fatiamento

Dados2 = {}
ListaDeGols2 = [1,2,3]
Dados2["Gols"] = ListaDeGols2[:]

ListaDeGols2.append(9)
print("Dicionario e liista com tecnica do fatiamento apos ser adicionado um valor a lista simples")
print(Dados2)
print(ListaDeGols2)

#CUIDADO: o link so acontece quando atualizamos a lista simples fora da estrutura utilizando o metodo .append() caso seja utilizado outra forma de atualizacao o link da lista nao sera atualizado. Eis um exemplo:
print("\n")
print("=-" * 30)
print(f"{"SO PODEMOS USAR O CONCEITO DO LINK UTILIZANDO O METODO .APPEND()":^55}")

Dados3 = {}
ListaDeGols3 = [3, 2, 1]

Dados3["Gols"] = ListaDeGols3

print("Dicionario com lista de gols antes da atualizacao: ")
print(Dados3)

#Agora vamos atualizar a lista simples fora da estrutura pela teoria a liista dentro da estrutura tambem deveria ser atualizada
ListaDeGols3 = [9, 2, 8]

#Perceba no print que o dicionario nao foi atualizado com os valores acima
print("Dicionario com lista de gols apos a atualizacao: ")
print(Dados3)

#Restabelencendo a lista e reatribuindo-a ao dicionario e utilizando o metodo append podemos notar que a lista e atualizada
ListaDeGols3 = [1, 2, 3]
Dados3["Gols"] = ListaDeGols3
ListaDeGols3.append(9)

print("Dicinario com lista de gols apos ser utilizado o metodo .append(): ")
print(Dados3)



#OBS: Caso eu nao tivesse reestabelecido a lista ela o dicionario nao atualizava com o metodo append. Tenho que estudar isso depois mas por enquanto tudo acima esta correto
#CONCLUSAO: Deve-se sempre utiilizar o fatiamento quando estamos passando uma lista para outra estrutura


#No exercicio 93 as lista simples ficara linkada com a lista do dicionario! O link so eh percebido quando utilizamos o metodo .append() posteriormente a atribuicao da liista siimples ao dicionario, como mostrado no exemplo da aula 19. Durante o exercicio 93 apos atribuir a lista simples ao dicionario tentei provar a existencia do link alterando a lista com 'ListaDeGols = [9,8,7]' porem por algum motiivo isso nao modifica a lista dentro do dicionario, o que modificaria eh utilizar o comando .append(). Ou seja, se nao houver o fatiamento da lista durante a atribuicao dela a outra estrutura ambas as listas ficarao linkadas

#Caso o fatiamento nao seja inserido quando estamos atribuindo a lista simples a lista composta tudo que for alterado na lista simples, mesmo depois da atribuicao, tambem sera alterado na lista composta.
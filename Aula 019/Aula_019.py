#DICIONARIOS

#Estrutura basica de um dicionario
Pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

#Pode-se pensar nos dicionarios como listas compostas, porem ao invez das listas simples serem referenciadas atravez de um numero elas sao referenciadas atravez do nome dado a elas

#Exibindo todo o dicionario
print("Exibindo todo o dicionario:")
print(Pessoas)
print("\n")


#Exibindo apenas um elemento do dicionario
print("Exibindo apenas um elemento do dicionario:")
print(Pessoas['nome'])
print("\n")

#Exibindo os elementos atravez de um print formatado
#Obs: no video eh utilizado aspas simples para referenciar a mensagem inteira e aspas duplas para referenciar o elemento desejado da biblioteca, caso ocorra algum erro futuro verificar isso
print("Fazendo um print formatado com os dicionarios")
print(f"O {Pessoas["nome"]} tem {Pessoas["idade"]} anos.")
print("\n")


#Exibindo apenas o nome das 'variaveis' dentro do dicionario (chamadas aqui de keys)
print("Exibindo apenas as 'variaveis criadas' para o dicionario (chamadas aqui de keys):")
print(Pessoas.keys())
print("\n")

#Exibindo apenas os valores armazenados nas keys
print("Exibindo apenas os valores armazenados nas keys:")
print(Pessoas.values())
print("\n")

#Mostransdo a composicao de elementos da estrutura de dicionario (basicamente exibindo todo o dicionario)
#Perceba que a estruttura eh uma lista de tuplas, uma para cada key
print("Mostrando a composicao de elementos da estrutura de dicionario (basicamente exibindo todo o dicionario):")
print(Pessoas.items())
print("\n")

#Acessando as keys atravez de loops
print("Acessando as keys atravez de loops:")
for i in Pessoas.keys():
    print(i)
print("\n")

#Exibindo todo o dicionario (keys e valores) atravez de loops
#Obs: perceba que aqui precisamos de duas variaveis
print("Exibindo todo o dicionario (keys e valores) atravez de loops:")
for i, j in Pessoas.items():
    print(f"{i} = {j}")
print("\n")

#Apagando umas das keys da lista
print("Apagando uma das keys da lista")
del Pessoas['sexo']
for i, j in Pessoas.items():
    print(f"{i} = {j}")
print("\n")

#Colocando dicionarios dentro de uma lista
print("Colocando uma lista dentro de um dicionario")
Brasil = []
Estado1 = {"uf": "Rio de janeiro", "Sigla": "RJ"}
Estado2 = {"uf": "Sao paulo", "Sigla": "SP"}
Brasil.append(Estado1)
Brasil.append(Estado2)
print(Brasil)
print("\n")

#Ou seja dicionarios nada mais sao do que listas com nomes
print(f"Referenciando um determinado elemento dentro de um determinado dicionario:\n{Brasil[0]['uf']}")
print("\n")

#Copiando mais de um dicionario (quando inserido pelo usuario manualmente) ao invez de usar fatiamento como em listas aqui usaremos o metodo copy

FlagInsercaoManual = input("Deseja continuar para a parte de inserir valores manualmente? (s/n): ").lower()

#Copiando mais de um dicionario (quando inserido pelo usuario manualmente) ao invez de usar fatiamento como em listas aqui usaremos o metodo copy
if FlagInsercaoManual == 's':
    Estado3 = dict()
    Brasil2 = list()
    for c in range(0, 3):
        Estado3['uf'] = str(input('Unidade Federativa: '))
        Estado3['Sigla'] = str(input("Sigla do Estado: "))
        Brasil2.append(Estado3.copy())
    print("\n")
    print("Exibindo todos os dicionarios da lista:")
    print(Brasil2)
    print("Exibindo os items utilizando o loop for: ")
    for e in Brasil2:
        for v in e.values():
            print(v)



#Lembrando que para atribuir uma dicionario a outra estrutura e preciso utiilizar o metodo .copy()
#Notas: Dicionarios são listas em que referenciamos os indices por nomes e nao por numeros

#CONCEITO IMPORTANTE PARA ESTRUTURAS DE ARMAZENAMENTO
#Notas2: Para adicionarmos um elemento a uma lista simples utilizamos .append() ou .insert | Para adicionarmos uma lista simples a outra estrutura utilizamos .appen([:]) com fatiamento | Para adicionarmos um dicionario a outra estrutura utilizamos o metodo .copy

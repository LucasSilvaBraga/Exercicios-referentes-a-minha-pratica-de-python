#LISTAS COMPOSTAS

#Aparenta ser o mesmo que matriz, se voce colocar os exemplos dados no video em um tabela com linha e colunas vai bater

#ADICIONANDO UMA LISTA DENTRO DE OUTRA PARA CRIAR UMA LISTA COMPOSTA
#Criando a lista 'teste' e adicionando dois elementos a ela
Teste = []
Teste.append('Gustavo')
Teste.append(40)

#Criando uma lista 'Galera' e colocando lista 'teste' dentro dela
Galera = []
Galera.append(Teste[:])
print(Galera)
print(Teste)

#Colocando 2 novos elementos na lista 'teste'
Teste[0] = 'Maria'
Teste[1] = 22

#Adicionando mais essa lista a lista composta 'teste'
#Lembrando que, sempre devemos utilizar um fatiamento quando estamos igualando uma lista a outra. No caso aqui foi feito o fatiamento completo "[:]"
Galera.append(Teste[:])
print(Galera)
print(Teste)




#UTILIZANDO INDICES PARA RETORNAR DETERMINADOS ELEMENTOS NA LISTA COMPOSTA
Galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print("\n\n")

#Sera printado a lista na posicao 2 com seu respctivo item da posicao 1
#Repare que tambem podemos enxergar como uma matriz de 3 linhas representando cada amostra ou cada pessoa, e 2 colunas sendo a primeira representando nome e a segunda representando idade
print("Printando um item especifico da lista composta:")
print(Galera[2][1])


#Utilizando um loop for sera printado cada indice da lista composta (cada lista da lista composta). Ou tambem cada linha da matriz
print("Printando cada lista da lista composta utilizando o loop for:")
for p in Galera:
    print(p)

print("\n")

#Fazendo um sistema de registro utilizando o loop for
Galera = []
Dado = []
for c in range(0, 3):
    Dado.append(str(input("Nome: ")))
    Dado.append(int(input("Idade: ")))

    #Lembrando sempre de inserir o fatiamento ao final da lista, caso nao estivessemos usando o fatiamento criariamos as linhas da nossa matriz, porem todas as colunas estariam vazias
    Galera.append(Dado[:])

    #Utilizando o metodo clear para apagar a lista simples utilizada apenas para ser copiado para a lista composta a cade vez que os dados sao copiados
    Dado.clear() 

print("\n")

#Se a coluna 1 da respectiva linha p for maior que 21 o print ocorrera
TotalMaior = TotalMenor = 0
for p in Galera:
    if p[1] >= 21:
        print(f"{p[0]} eh maior de idade.")
        TotalMaior += 1
    else:
        print(f"{p[0]} eh menor de idade.")
        TotalMenor += 1    

print(f"Temos {TotalMaior} maiores e {TotalMenor} menores de idade")
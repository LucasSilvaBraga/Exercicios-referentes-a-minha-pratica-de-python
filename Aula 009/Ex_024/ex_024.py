#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÇAO COM O NOME 'SANTO'

Nome = str(input("Digite o nome de uma cidade: "))
Nome = Nome.lower()
#removendo os espacos
Nome = Nome.strip()

print(Nome[:5] == 'santo')
#Em 'Nome[:5]' sera lido as 5 primeiras letras da string digitada, em '== 'santo' ' caso as 5 primeiras letras correspondam a palavra santo o print exibira um 'true'
#Ou seja, em python os prints podem possuir condicionais  
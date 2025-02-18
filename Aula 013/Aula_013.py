#-----Estrutura de repeticao for-----

#Modelo Basico
for c in range(1, 6):
    print("oi")
print("fim")

#Ou seja: A variavel 'c' comeca em um e vai ate 6
#Correspondente a: for(c = 1; c < 6; c++)

#Podemos ate printar a propria variavel que esta sendo loopada
for c in range(0, 6):
   print(c)

#Para que ele loop de tras para frente 
for c in range(6, 0, -1):
    print(c)
#Ou seja, a sintaxe eh: for 'Variavel_contadora' in range('Valor_inicial_da_variavel_contadora', 'condicao de parada', 'Iteracao')
#Iteracao --> ato de iterar; repetição. 'Nada' para somar '-1' para subtrair
#Corresponde a: for(c=6; c < 0; c--)


#Repare que em linguagem C a estrutura de repeticao se baseia em 
#for('condicao_incial', 'condicao_de_parada', 'passo')
#Se tivermos for(i=0; i<6; i++)
#A condicao vai ser repetida enquanto i for menor que 6, vai parar em 5 pois eh o ultimo numero menor que 6

#Um outro ler tuplas (e tambem listas) eh:
ListaDePrecos = (5000, 2000, 200, 50)

print("Um outro ler tuplas (e tambem listas) eh: ")

#Le-se: para cada 'preco' em 'lista de precos'
#Mas preco poderia ser qualquer outra variavel com 'i' o que acontece e que o python atribui cada um dos itens a variavel preco, fazendo todas as acoes dentro da identacao em cada para cada item (que foi ou sera armazenado dentro da variavel preco)
for preco in ListaDePrecos:
    print(preco)


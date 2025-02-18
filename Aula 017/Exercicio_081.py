#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

FlagContinuar = ""
Contador = 0
Lista = []
ValorMaiorQueInserido = 0
EstaNaLista = 0

#Loop para inserir valores na lista
while FlagContinuar != "n":

    Contador = len(Lista) - 1

    #Requisita o numero para o usuario
    Numero = int(input("Digite um numero para ser adicionado a lista: "))

    #Loop infinito que so sera interrompido quando o valor for adicionado
    while True:
        #Se Contador for = a -1 existem duas opcoes, ou eh o primeiro item a ser adicionado na lista, ou a lista foi percorrida ate o final e nao foi encontrado um valor maior que o digitado (O algoritimo busca o primeiro valor maior do que o digitado, quando o encontra adiciona o novo numero a direita desse valor)
        if Contador == -1:
            Lista.insert(0, Numero)
            break

        #Acha a posicao do primeiro valor maior do que o digitado e adiciona ele a direita desse (Como o metodo insert sempre adiciona o novo elemento a esquerda da posicao solicitado, somamos + 1 a posicao para que op novo numero seja adicionado a esquerda do numero anterior, fazendo assim que o posicao seja a correta)
        if Lista[Contador] > Numero:
            Lista.insert(Contador + 1, Numero)
            break

        #Contador se inicia no ultimo elemento da lista, percorrendo ela de tras para frente, o primeiro maior valor que encontrarmos sera sempre a posicao correta para adicionar o novo valor (ficara sempre a direita do primeiro numero que for maior que ele)    
        Contador -= 1
    print(Lista)
        
    #Flag para parar de digitar valores
    FlagContinuar = input("Deseja continuar a digitar valores? (s/n): ")
    while FlagContinuar != 's' and FlagContinuar != "n":
        FlagContinuar = input("Digite uma opcao valida. Deseja continuar? (s/n): ")
        

    Contador += 1

#Verificando se o valor 5 esta na lista
for i in range (0, len(Lista)):
    if Lista[i] == 5:
        EstaNaLista = 1

if EstaNaLista == 1:
    print("O numero 5 esta na lista")
else:
    print("O numero 5 nao esta na lista")
print(f"A lista de valores digitados foi {Lista}")
print(f"A quantidade de valores digitados foi: {len(Lista)}")



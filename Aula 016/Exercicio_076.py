#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos, na sequencia. No final, mostre uma listagem de precos, organizando os dados em forma tabular
Distancia = 30
Maior = 0

Lista = ("Lapis", 1.75, "Borracha", 2.00, "Caderno", 15.00, "Estojo", 25.00, "Transferidor", 4.20)

for j in range(0, len(Lista)):
        if j % 2 != 0:
            if Lista[j] > Maior:
                Maior = Lista[j]

TamanhoMaiorValor  = len(str(Maior)) + 1
print(f"Tamanho maior valor: {TamanhoMaiorValor}")


#A lista tera sempre um valor par
for i in range(0, (len(Lista))):

    

    if i % 2 != 0:
        Pontinhos = Distancia - (len(Lista[i - 1]))
        print(Pontinhos * ".", end ='')

        TamanhoValorAtual = len(str(Lista[i]))
        if i == 1:
            TamanhoValorAtual -= 1
        Espacos = TamanhoMaiorValor - TamanhoValorAtual
        print("R$", end = '')
        print(Espacos * " ", end = '')
        print(f"{Lista[i]:.2f}")
    else:
        print(Lista[i], end = '')


#=-=-=-=-=-=-GABARITO-==-=-=-==-=-=-=-=-
Lista = ("Lapis", 1.75, "Borracha", 2.00, "Caderno", 15.00, "Estojo", 25.00, "Transferidor", 4.20)

print('-' * 40)
#Perceba que eh inserido uma aspas dentro do colchete para conseguir formatar
#Tambem utilizamos ':^40' para centralizar com 40 espacos de cada lado
print(f'{"LISTAGEM DE PRECOS":^40}')
print('-' * 40)

for i in range(0, len(Lista)):
     if i == 0:
          #aqui a formatacao eh ':.<30' o texto ja foi previamente alinhado a esquerda e depois forama alinhados pontos tambem a esquerda num limite de 30 caracteres
          print(f'{Lista[i]:.<30}')
     else:
          #Printando o valor alinhado a esquerda com limite de 7 caracteres e '.2f' para aparecer os numeros centavos
          print(f'R${Lista[i]:>7.2f}')


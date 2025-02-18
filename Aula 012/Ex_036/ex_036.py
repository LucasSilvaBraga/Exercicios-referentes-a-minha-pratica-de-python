#ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO 

ValorCasa = float(input("Digite o valor do imovel: "))
Salario = float(input("Digite o salario do comprador: "))
Tempo = float(input("Dite em quanto tempo esse valor sera pago: "))

ValorMensal = (ValorCasa / Tempo) / 12

if Salario * 0.3 < ValorMensal:
    print("Emprestimo negado!")
else:
    print("Emprestimo aceito!")



#-----Resolucao incorreta-----

#if Salario * 0.3 < ValorMensal:
#    print("Emprestimo negado!")
#   
#print("Emprestimo aceito!")

#Aqui serao exibidas as duas mensagens pois mesmo a condicao sendo verdadeira o codigo ainda continua depois dessa verificacao

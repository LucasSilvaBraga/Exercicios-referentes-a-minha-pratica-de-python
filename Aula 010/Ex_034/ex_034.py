#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIIO E CALCULE O VALOR DO SEU AUMENTO.
#PARA SALÁRIOS SUPERIORES A  1250.00, CALCULE UM AUMENTO DE 10% PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%

Salario = float(input("Qual eh o valor do seu salario: "))

if Salario > 1250:
    print("O seu novo salario sera: {}". format(Salario * 1.1))
else:
    print("O seu novo salario sera de: {}". format(Salario * 1.15))

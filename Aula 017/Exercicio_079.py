#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
#Exercicio feito por mim mesmo

Lista = []
FlagParar = ""
Contador = 0
NumeroRepetido = False


while(FlagParar != "n"):

    if Contador == 0:
        Lista.append(int(input("Digite um valor: ")))
        #Flag para verificar se o usuario ainda deseja continuar digitando numeros
        FlagParar = input("Deseja continuar a digitando numeros? (s/n): ")
        while FlagParar != "n" and FlagParar != "s":
            FlagParar = ""
            FlagParar = input("Digite uma opcao valida. Deseja continuar a digitando numeros? (s/n): ")


    else:
        Lista.append(int(input("Digite uma valor: ")))
        for i in range (0, Contador):
            if Lista[i] == Lista[Contador]:
                NumeroRepetido = True
        if NumeroRepetido == True:
            Lista.pop()
        while NumeroRepetido == True:
            Lista.append(int(input("Esse numero ja foi digitado digite um outro numero: ")))
            NumeroRepetido = False
            for i in range (0, Contador):
                if Lista[i] == Lista[Contador]:
                    NumeroRepetido = True
            if NumeroRepetido == True:
                Lista.pop()
            

        #Flag para verificar se o usuario ainda deseja continuar digitando numeros
        FlagParar = input("Deseja continuar digitando numeros? (s/n): ")
        while FlagParar != "n" and FlagParar != "s":
            FlagParar = ""
            FlagParar = input("Digite uma opcao valida. Deseja continuar digitando numeros? (s/n): ")

    Contador += 1
Lista.sort()
print(f"Voce digitou os valores: {Lista}")

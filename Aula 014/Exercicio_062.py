#Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 termos

PrimeiroTermo = int(input("Digite o valor do primeiro termo da PA: "))
Razao = int(input("Digite a razao da PA: "))
Contador = 9
ContadorTermos = 0

print("{} -> ". format(PrimeiroTermo), end = '')
Soma = PrimeiroTermo + Razao
ContadorTermos += 2
print("{} -> ". format(Soma), end = '')


while Contador != 0:
    while Contador > 1:
        Soma = Soma + Razao
        ContadorTermos += 1
        print("{} -> ". format(Soma), end = '')
        Contador -= 1
    print("Fim")
    print("Total de termos: {}". format(ContadorTermos))
    Contador = int(input("Quer mostrar fazer mais termos? Se sim basta digitar quantos termos a mais deseja, se nao basta digitar 0: "))
    if Contador != 0:
        Contador += 1
    

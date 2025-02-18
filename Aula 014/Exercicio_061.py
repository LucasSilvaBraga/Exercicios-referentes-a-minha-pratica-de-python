#Refaca o desafio 051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while

Cont = 9
PrimeiroTermo = int(input("Digite o primeiro termo da PA: "))
Razao = int(input("Digote a razao da PA: "))

Produto = PrimeiroTermo + Razao
print("{} -> ". format(PrimeiroTermo), end='')
while Cont > 0:
    print("{} -> ". format(Produto), end='')
    Produto = Produto + Razao
    Cont -= 1
   
print("Fim!")



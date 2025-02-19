#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

ParentesesEsquerda = 0
ParentesesDireita = 0

#Podemos considerar a string como uma lista de caracteres assim como em linguagem c
Expressao = str(input("Digite a sua expressao: "))

for i in range (0, len(Expressao)):
    if Expressao[i] == '(':
        ParentesesEsquerda += 1
    if Expressao[i] == ')':
        ParentesesDireita += 1
if ParentesesDireita == ParentesesEsquerda:
    print("Sua expressao esta correta")
else:
    print("Sua expressao esta incorreta")


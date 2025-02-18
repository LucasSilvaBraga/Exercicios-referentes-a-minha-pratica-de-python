#FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO

import math

Angulo = float(input("Digite o valor de qualquer angulo: "))

#Para extrair uma angulo com a biblioteca math deve-se passar o valor para radianos
AnguloRadianos = math.radians(Angulo)

print("O seno do angulo {} eh: {:.2f}". format(Angulo, math.sin(AnguloRadianos)))
print("O cosseno do angulo {} eh: {:.2f}". format(Angulo, math.cos(AnguloRadianos)))
print("A tangente do angulo {} eh: {:.2f}". format(Angulo, math.tan(AnguloRadianos)))



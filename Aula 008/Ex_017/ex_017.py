#FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

import math

CatetoOposto = float(input('Digite o comprimento do cateto oposto: '))
CatetoAdjacente = float(input('Digite o comprimentod o cateto adjacente: '))
Hipotenusa = math.sqrt((CatetoOposto**2) + (CatetoAdjacente**2))

print("O valor da hipotenusa desse triangulo eh: {}". format(Hipotenusa))

#====FAÇA UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE EM METROS, CALCULE SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA,
#SABENDO QUE CADA LITRO DE TINTA PINTA 2M²====

Altura = float(input('Digite a altura da sua parede: '))
Largura = float(input('Digite a largura da sua parede: '))

Area = Altura * Largura

print('A area da sua parede eh de: {}'. format(Area))
print('A quantidade de litros necessaria para pintar essa area eh de: {}'. format(Area/2))
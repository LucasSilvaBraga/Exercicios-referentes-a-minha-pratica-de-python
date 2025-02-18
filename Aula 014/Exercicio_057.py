#Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'm' e 'f'. Caso esteja errado, peca a digitacao novamente ate ter um valor correto


Genero =''

Genero = input("Digite seu genero (M/F): ").upper()

while Genero != 'M' and Genero != 'F':
    print("Digite uma opcao valida")
    Genero = input("Digite seu genero (M/F): ").upper()
    
print("Opcao aceita!!")

#=====MANEIRA INCORRETA=====

#while Genero != 'M' or Genero != 'F':
    #Genero = str(input("Digite seu genero (M/F): ")).upper()
    #print(Genero)

#Caso o input seja = 'm' o prompt mostrara 'Digite uma opcao valida'

#O caso gera estranheza pois semanticamente a afirmacao "enquanto genero for diferente de 'm' ou de 'f'" parece correta mas nao eh.
# O correto seria "Enquanto genero for diferente de 'm' e tambem dferente de 'f'". Assim o que for digitado precisa ser diferente de m e f

#Para evitar essa confusao sempre ler estruturas de controle como. "Para tal coisa acontecer uma dessas condicoes deve ser atendida (No caso de OR)" 
# Ou "Uma dessas condicoes deve ser atendida (no caso do AND)"

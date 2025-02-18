#Crie um programa que faca o computador jogar jokenpo com voce
# 1 = pedra
# 2 = papel
# 3 = tesoura


from random import choice
from time import sleep 

Usuario = int(input("Qual a sua escolha:\n[1]Pedra\n[2]Papel\n[3]Tesoura\n"))
Bot = choice([1 , 2, 3])

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

if Usuario == 1 and Bot == 1:
    print("Usuario: Pedra\n X Bot: Pedra\nEMPATE!!!") 
elif Usuario == 1 and Bot == 2:
    print("Usuario: Pedra\n X Bot: Papel\nVITORIA DO BOT!!!") 
elif Usuario == 1 and Bot == 3:
    print("Usuario: Pedra\n X Bot: Tesoura\nVITORIA DO Usuario!!!")
elif Usuario == 2 and Bot == 1:
    print("Usuario: Papel\n X Bot: Pedra\nVITORIA DO USUARIO!!!") 
elif Usuario == 2 and Bot == 2:
    print("Usuario: Papel\n X Bot: Papel\nEMPATE!!!")
elif Usuario == 2 and Bot == 3:
    print("Usuario: Papel\n X Bot: Tesoura\nVITORIA DO BOT!!!")
elif Usuario == 3 and Bot == 1:
    print("Usuario: Tesoura\n X Tesoura: Pedra\nVITORIA DO BOT!!!")
elif Usuario == 3 and Bot == 2:
    print("Usuario: Tesoura\n X Bot: Papel\nVITORIA DO USUARIO!!!") 
elif Usuario == 3 and Bot == 3:
    print("Usuario: Tesoura\n X Bot: Tesoura\nEMPATE!!!")






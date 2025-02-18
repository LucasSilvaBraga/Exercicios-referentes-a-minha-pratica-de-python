#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
#SE ELE AINDA  VAI SE ALISTAR AO SERVIÇO MILITAR
#SE É HORA DE SE ALISTAR
#SE JÁ PASSOU DO TEMPO DO ALISTAMENTO
#SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO 
#alistamento militar começa no dia primeiro de janeiro apos o cidadao completar 18 anos

#Importando e utilizando a biblioteca datetime para extrair data atual do sistema do usuario
from datetime import datetime

DataAtual = datetime.now()

DiaAtual = DataAtual.day
MesAtual = DataAtual.month
AnoAtual = DataAtual.year

#Extraindo as informacoes do usuario
Dia = int(input("Digite o dia do seu nascimento: "))
Mes = int(input("Digite o mes do seu nascimento: "))
Ano = int(input("Digite o ano do seu nascimento: "))

#Caso o o cidadao esteja completando 18 anos no ano atual e esteja dentro do prazo
if AnoAtual - Ano == 18:
    print("Seu alistamento militar comeca no dia 01/01/{} e termina 30/06/{}". format(AnoAtual + 1, AnoAtual + 1))

#Caso o cidadao nao esteja completando 18 anos no ano atual
elif AnoAtual - Ano <= 17:
    AnoAlistamento = Ano + 19
    print("Voce nao completa 18 anos esse ano, seu alistamento podera ser efetuado do dia 01/01/{} ate 30/06/{}". format(AnoAlistamento, AnoAlistamento))
#Caso o cidadao ja tenha completado 18 anos e tenha perdido a primeira chamada do alistamento
elif AnoAtual - Ano >= 19:
    if(MesAtual < 7):
        print("Voce esta atrasado, aliste-se agora! O alistamento acaba em 30/06/{}". format(AnoAtual))
    else:
        print("Voce esta atrasado e o prazo do alistamento desse ano ja acabou, aliste-se em 01/01/{} ate 30/06/{}". format(AnoAtual + 1, AnoAtual + 1))



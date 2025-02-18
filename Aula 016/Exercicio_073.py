#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocacao. Depois mostre:
#Os 5 primeiros 
#Os ultimos 4 colocados
#Times em ordem alfabetica
#Em que posicao esta o time da chapecoense

Times = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "Sao Paulo", "Corinthians",
         "Bahia", "Cruzeiro", "Vasco", "Vitoria", "Atletico Mineiro", "Fluminense", "Gremio", "Juventude",
         "Bragantino", "Athletico Paranaense", "Criciuma", "Atletico Goianiense", "Cuiaba")

print("Os 5 primeiros colocados sao:")
for i in range(0, 5):
    print("{}\n". format(Times[i]))

print("Os ultimos 4 colocados sao: ")
for i in range (16, 20, 1):
    print("{}\n". format(Times[i]))

print("Os times que estao na serie A sao: ")
for i in sorted(Times):
    print(i)

print("A posicao do Vasco eh:")
print(Times.index("Vasco"))




    



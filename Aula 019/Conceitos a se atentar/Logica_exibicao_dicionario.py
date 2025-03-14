Brasil = [{"uf": "SP", "Nome" : "sao paulo"}, {"uf": "ES", "Nome" : "espirito santo"}, {"uf": "RJ", "Nome" : "rio de janeiro"}]


#Brasil eh uma lista de dicionarios
#No primeiro for 'i' assumira o valor de cada item da lista, ou seja vai referenciar cada dicionario individualmente
#Como 'i' agora referencia um dicionario utilizamos o metodo 'items()' para que seja retornado keys e valores do determinado 'i'. Os valores retornados serao armazenados nas variaveis 'k' e 'v'

for i in Brasil:
    for k, v in i.items():
        print(f"{k}: {v}")
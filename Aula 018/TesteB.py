#E possivel dar break no for

ListaNumeros = [1, 2, 5, 6]
Numero = 3

for i in range (0, len(ListaNumeros)):
    if ListaNumeros[i] > Numero:
        ListaNumeros.insert(i, Numero)
        break

print(ListaNumeros)

#E sim!
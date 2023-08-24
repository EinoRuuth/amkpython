def parilliset(lista):
    lista2 = []
    for x in lista:
        if x % 2 == 0:
            lista2.append(x)
    return lista2

lista=[2, 6, 5, 8, 3, 7, 10, 25, 40]
print(parilliset(lista))

lista = []
indeksi = 0
while True:
    luku = input("Anna numero: ")
    print(lista)
    if luku == "":
        lista.sort(reverse=True)
        for x in range(5):
            print(lista[indeksi])
            indeksi =indeksi+1
        exit(1)
    lista.append(int(luku))

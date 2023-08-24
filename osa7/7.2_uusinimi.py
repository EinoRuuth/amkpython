lista = []

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    if nimi in lista:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        lista.append(nimi)

for x in lista:
    print(x)

joukko = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    if nimi in joukko:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        joukko.add(nimi)

for x in joukko:
    print(x)

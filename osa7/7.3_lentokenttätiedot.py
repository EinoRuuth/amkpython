sanakirja = {}

while True:
    valinta = input("Haluatko syöttää uuden lentoaseman (1) vai hakea syötettyä (2) vai lopettaa (3): ")
    if valinta == "3":
        break
    elif valinta == "1":
        nimi = input("Syötä lentoaseman nimi: ")
        icao = input("Syötä ICAO koodi: ")
        sanakirja[icao] = nimi
    elif valinta == "2":
        icaohaku = input("Syötä ICAO koodi: ")
        print(sanakirja[icaohaku])

ktunnus = "python"
ksalasana = "rules"

kertaa = 0

while True:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == ktunnus and salasana == ksalasana:
        print("Tervetuloa!")
        exit(1)
    else:
        print("Pääsy evästetty")
    kertaa = kertaa+1
    if kertaa == 5:
        print("Liian monta yritystä")
        exit(1)

class julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class kirja(julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" kirja: nimi:{self.nimi}, kirjailija: {self.kirjoittaja}, sivumäärä: {self.sivumäärä} sivua")

class lehti(julkaisu):

    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" lehti: nimi: {self.nimi}, päätoimittaja: {self.päätoimittaja}")


työntekijät = []
työntekijät.append(lehti("Aku Ankka", "Aki Hyyppä"))
työntekijät.append(kirja("Hytti n:o 6", "Rosa Liksom", 200))

for t in työntekijät:
    t.tulosta_tiedot()
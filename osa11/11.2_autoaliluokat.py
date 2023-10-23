class auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matka=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    
    def kulje(self, aika):
        self.matka = self.nopeus*aika
        return

    def tulosta_tiedot(self):
        print (f"{self.rekkari}:")

class Polttomoottoriauto(auto):
    def __init__(self, rekkari, huippunopeus, bensatankki, nopeus=0, matka=0):
        self.bensatankki = bensatankki
        super().__init__(rekkari, huippunopeus, nopeus, matka)
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" ajettu matka:{self.matka}")

class sähköauto(auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti, nopeus=0, matka=0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekkari, huippunopeus, nopeus, matka)
    
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" ajettu matka:{self.matka}")
    
autot = []
autot.append(sähköauto("ABC-15", 180, 52.5, 130))
autot.append(Polttomoottoriauto("ABC-123", 165, 32.3, 100))

for c in autot:
    c.kulje(3)
    c.tulosta_tiedot()
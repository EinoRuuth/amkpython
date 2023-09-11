import random as rd

class auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matka=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    
    def kiihdytä(self, nopeus):
        if self.nopeus + nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = self.nopeus + nopeus
        return
    
    def kulje(self, aika):
        self.matka = self.matka + self.nopeus*aika
        return
    

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tuntikuluu(self):
        for x in self.autot:
            x.kiihdytä(rd.randint(-10,15))
            x.kulje(1)
        return
    
    def tulostatilanne(self, loppu):
        if loppu:
            print("tilanne:")
        for x in self.autot:
            print (f"auto:{x.rekkari:s} matka:{x.matka}km")
        return
    
    def kilpailuohi(self):
        for x in self.autot:
            if x.matka >= self.pituus:
                return True
        return False
        

lista = ["auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7", "auto8", "auto9", "auto10"]

for x in range(10):
    rekkari = "ABC-"+str(x+1)
    hnopeus = rd.randint(100,200)
    lista[x] = auto(rekkari, hnopeus)

kisa = Kilpailu("Suuri romuralli", 8000, lista)

while True:
    for x in range(10):
        kisa.tuntikuluu()
        ohi = kisa.kilpailuohi()
        if ohi == True:
            break
    if ohi == True:
            break
    kisa.tulostatilanne(True)

print("lopputilanne:")
kisa.tulostatilanne(False)

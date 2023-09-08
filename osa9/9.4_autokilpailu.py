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

lista = ["auto1", "auto2", "auto3", "auto4", "auto5", "auto6", "auto7", "auto8", "auto9", "auto10"]

for x in range(10):
    rekkari = "ABC-"+str(x+1)
    hnopeus = rd.randint(100,200)
    lista[x] = auto(rekkari, hnopeus)

jatka = True

while jatka:
    for x in lista:
        if x.matka >= 10000:
            jatka = False
        x.kiihdytä(rd.randint(-10,15))
        x.kulje(1)

for x in lista:
    print (f"auto:{x.rekkari:s} matka:{x.matka}km")

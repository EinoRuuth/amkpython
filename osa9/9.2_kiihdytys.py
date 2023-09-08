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
    

auto1 = auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
auto1.kiihdytä(-200)
print (f"rekkari:{auto1.rekkari:s} huippunopeus:{auto1.huippunopeus:d} nopeus:{auto1.nopeus}")

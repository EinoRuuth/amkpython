class auto:
    def __init__(self, rekkari, huippunopeus, nopeus=0, matka=0):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    

auto1 = auto("ABC-123", 142)

print (f"rekkari:{auto1.rekkari:s} huippunopeus:{auto1.huippunopeus:d} nopeus:{auto1.nopeus} matka:{auto1.matka}")

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin
        pass
    
    def siirry_kerrokseen(self, kerros, hissi):
        if kerros > self.kerros:
            for x in range(kerros - self.kerros):
                hissi.kerros_ylös()
        elif kerros < self.kerros:
            for x in range(self.kerros - kerros):
                hissi.kerros_alas()
        return
    
    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        return
    
    def kerros_alas(self):
        self.kerros = self.kerros - 1
        return
    
class Talo:
    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for x in range(hissit):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)
        pass
    
    def ajaa_hissiä(self, hissi, kerros):
        hissi2 = self.hissit[hissi-1]
        hissi2.siirry_kerrokseen(kerros, hissi2)
        print(f"hissi:{hissi} on nyt kerroksessa:{hissi2.kerros}")
        return
    
    def palohälytin(self):
        print("palohälytys!")
        for x in range(len(self.hissit)):
            t.ajaa_hissiä(x+1, 0)
        return


t=Talo(0, 10, 4)

t.ajaa_hissiä(1, 3)
t.ajaa_hissiä(2, 5)
t.ajaa_hissiä(3, 2)
t.ajaa_hissiä(4, 10)


t.ajaa_hissiä(1, 7)
t.ajaa_hissiä(2, 9)
t.ajaa_hissiä(3, 6)

t.palohälytin()

class hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin
        pass
    
    def siirry_kerrokseen(self, kerros):
        if kerros > self.kerros:
            for x in range(kerros - self.kerros):
                h.kerros_ylös()
        elif kerros < self.kerros:
            for x in range(self.kerros - kerros):
                h.kerros_alas()
        return
    
    def kerros_ylös(self):
        self.kerros = self.kerros + 1
        return
    
    def kerros_alas(self):
        self.kerros = self.kerros - 1
        return

h=hissi(0,10)

h.siirry_kerrokseen(9)
print(h.kerros)
h.siirry_kerrokseen(0)
print(h.kerros)

import math

def worttilaskuri(pizza, hinta):
    alue = math.pi * pizza
    return alue / hinta

ekapizza = float(input("Anna pizzan halkaisija (cm): "))
ekahinta = float(input("Anna pizzan hinta (€): "))

tokapizza = float(input("Anna pizzan halkaisija (cm): "))
tokahinta = float(input("Anna pizzan hinta (€): "))

eka = worttilaskuri(ekapizza, ekahinta)
toka = worttilaskuri(tokapizza, tokahinta)

if eka > toka:
    print("Ekalla pizzalla on parempi hinta")
elif toka > eka:
    print("Toisella pizzalla on parempi hinta")


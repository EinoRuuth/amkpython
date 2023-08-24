leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

luoti = 13.3
naula = 32 * luoti
leiviskä = 20 * naula

luodit2 = luodit * luoti
naulat2 = naulat * naula
leiviskät2 = leiviskät * leiviskä
kaikki = luodit2 + naulat2 + leiviskät2

grammat = kaikki % 1000
kaikki = kaikki - grammat
kilogrammat = kaikki / 1000

kilogrammat = round(kilogrammat)
grammat = round(grammat, 2)

print(str(kilogrammat)+" kilogrammaa ja "+str(grammat)+" grammaa.")

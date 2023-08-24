import random as rd

maksimi = int(input("Anna nopan maksimisilmämäärä: "))

def noppa(luku2):
    luku = rd.randint(1,luku2)
    return luku

while True:
    luku = noppa(maksimi)
    print(luku)
    if luku == maksimi:
        break

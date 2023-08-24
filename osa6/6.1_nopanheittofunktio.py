import random as rd

def noppa():
    luku = rd.randint(1,6)
    return luku

while True:
    luku = noppa()
    print(luku)
    if luku == 6:
        break

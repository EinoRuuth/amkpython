import random as rd
heitot = []
maara = int(input("Montako noppaa heitetään?: "))

for x in range(maara):
    noppa = rd.randint(1,6)
    heitot.append(noppa)

print("Noppien summa on "+str(sum(heitot)))

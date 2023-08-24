luku = int(input("Anna luku: "))

for x in range(2,100):
    if x != luku:
        if luku % x == 0:
            print("Luku "+str(luku)+" ei ole alkuluku")
            exit(1)

print("Luku "+str(luku)+" on alkuluku")

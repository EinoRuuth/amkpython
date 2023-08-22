import random as rd
numero = rd.randint(1,9)
while True:
    luku = int(input("Anna luku (1-9): "))
    if luku == numero:
        print("Arvasit luvun oikein!")
        exit(1)
    elif luku > numero:
        print("Liian suuri arvaus")
    elif luku < numero:
        print("Liian pieni arvaus")
luvut = []
while True:
    luku = input("Anna luku (tyhjä lopettaa): ")
    if luku == " ":
        pienin = min(luvut)
        suurin = max(luvut)
        print("pienin luku jonka annoit: "+str(pienin)+"\nsuurin luvun jonka annoit: "+str(suurin))
        exit(1)
    else:
        luvut.append(int(luku))

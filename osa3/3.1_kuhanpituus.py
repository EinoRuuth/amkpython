pituus = float(input("Anna kuhan pituus (cm): "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("kuhasta puuttuu pituutta "+str(puuttuu)+" cm. Laske kuha takaisin järveen.")
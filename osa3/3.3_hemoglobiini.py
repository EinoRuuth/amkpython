sukupuoli = input("Anna sukupuoli (Mies tai Nainen): ")
hemoglobiini = float(input("Anna hemoglobiini määrä: "))

if sukupuoli == "Mies":
    if hemoglobiini < 134:
        print("hemoglobiini on alhainen")
    elif hemoglobiini > 195:
        print("hemoglobiini on korkea")
    else:
        print("hemoglobiini on normaali")

if sukupuoli == "Nainen":
    if hemoglobiini < 117:
        print("hemoglobiini on alhainen")
    elif hemoglobiini > 175:
        print("hemoglobiini on korkea")
    else:
        print("hemoglobiini on normaali")

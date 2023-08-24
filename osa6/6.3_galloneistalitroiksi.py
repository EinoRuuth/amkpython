def muuntaja(gallons):
    litrat = gallons * 3.785
    return litrat

while True:
    luku = int(input("Anna gallonit: "))
    if luku < 0:
        break
    litroina = muuntaja(luku)
    print(litroina)

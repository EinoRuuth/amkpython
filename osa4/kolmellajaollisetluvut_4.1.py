numero = 1
while True:
    if numero % 3 == 0:
        print("numero "+str(numero)+" on jaollinen kolmella")
    if numero >= 1000:
        exit(1)
    numero = numero + 1
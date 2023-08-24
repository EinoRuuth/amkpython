tuuma = 2.54
while True:
    numero = float(input("Anna tuumat (negatiivinen lopettaa): "))
    if numero < 0:
        exit(1)
    else:
        sentit = numero * tuuma
        print(str(numero)+" tuumaa on "+str(sentit)+" cm.")

kevat = (3, 4, 5)
kesa = (6, 7, 8)
syksy = (9, 10, 11)
talvi = (12, 1, 2)

kuukausi = int(input("Anna kuukausi: "))
if kuukausi in kevat:
    print("Vuodenaika on kevät")
elif kuukausi in kesa:
    print("Vuodenaika on kesä")
elif kuukausi in syksy:
    print("Vuodenaika on syksy")
elif kuukausi in talvi:
    print("Vuodenaika on talvi")

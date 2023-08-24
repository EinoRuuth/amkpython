import random as rdm

eka = rdm.randint(0, 9)
toka = rdm.randint(0, 9)
kolmas = rdm.randint(0, 9)

kolmenumeroinen = str(eka) + str(toka) + str(kolmas)

eka2 = rdm.randint(1, 6)
toka2 = rdm.randint(1, 6)
kolmas2 = rdm.randint(1, 6)
neljas2 = rdm.randint(1, 6)

nelinumeroinen = str(eka2) + str(toka2) + str(kolmas2) + str(neljas2)

print("kolmenumeroinen koodi on: "+kolmenumeroinen+"\nnelinumeroinen koodi on: "+nelinumeroinen)
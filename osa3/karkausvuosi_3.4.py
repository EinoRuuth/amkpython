vuosi = int(input("Anna vuosi: "))
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print("vuosi on karkausvuosi")
    else:
        print("vuosi ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print("vuosi on karkausvuosi")
else:
        print("vuosi ei ole karkausvuosi")

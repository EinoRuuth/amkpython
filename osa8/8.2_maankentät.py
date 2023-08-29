import mysql.connector

sanakirja = {}

def hakija(maa):
    sql = "SELECT type FROM airport"
    sql += " WHERE iso_country='" + maa + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            if rivi[0] in sanakirja:
                sanakirja[rivi[0]] = sanakirja[rivi[0]] +1
            else:
                sanakirja[rivi[0]]=1
    for x in sanakirja:
        if x != "closed":
            print(f"{x}: {sanakirja[x]}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='admin',
         autocommit=True
         )

maakoodi = input("Anna maakoodi: ")
hakija(maakoodi)

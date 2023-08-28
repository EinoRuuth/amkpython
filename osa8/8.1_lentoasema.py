import mysql.connector

def hakija(icao):
    sql = "SELECT name, iso_region FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Lentoaseman nimi: {rivi[0]} ja kunta: {rivi[1]}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='admin',
         autocommit=True
         )

icaokoodi = input("Anna ICAO koodi: ")
hakija(icaokoodi)

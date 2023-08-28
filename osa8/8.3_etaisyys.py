import mysql.connector
from geopy import distance

def hakija(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='admin',
         autocommit=True
         )

icaokoodi = input("Anna ICAO koodi: ")
icaokoodi2 = input("Anna toinen ICAO koodi: ")

koordinaatit1 = hakija(icaokoodi)
koordinaatit2 = hakija(icaokoodi2)

koordinaatit1 = koordinaatit1[0]
koordinaatit2 = koordinaatit2[0]

pituus = (distance.distance(koordinaatit1, koordinaatit2).km)
pituus = round(int(pituus), 1)
print(f"lentokenttien väli on: {pituus}km")

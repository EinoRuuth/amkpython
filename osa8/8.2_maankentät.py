import mysql.connector

def hakija(maa):
    pienet = 0
    helikoperit = 0
    seaplane = 0
    medium = 0
    suuret = 0
    sql = "SELECT type FROM airport"
    sql += " WHERE iso_country='" + maa + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            if rivi[0] == "small_airport":
                pienet = pienet+1
            elif rivi[0] == "medium_airport":
                medium = medium+1
            elif rivi[0] == "large_airport":
                suuret = suuret+1
            elif rivi[0] == "heliport":
                helikoperit = helikoperit+1
            elif rivi[0] == "seaplane_base":
                seaplane = seaplane+1
    print(f"pieniä lentokenttiä: {pienet}\nkeskikokoisia lentokenttiä: {medium}\nsuuria lentokenttiä: {suuret}\nhelikopterikenttiä: {helikoperit}\nvesikonekentät: {seaplane}")
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

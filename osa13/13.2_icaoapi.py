from flask import Flask, request
import mysql.connector

def hakija(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            return (rivi[0], rivi[1])

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='admin',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    kenttätiedot = hakija(icao)
    print(kenttätiedot)
    return {"ICAO" : icao, "Name": kenttätiedot[0], "Municipality": kenttätiedot[1]}
    

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
import requests
import os
from dotenv import load_dotenv

paikkakunta = input("Anna paikkakunta: ")

load_dotenv()
apikey = os.getenv('apikey')
try:
    lokaatiokysely = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit=1&appid={apikey}"
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
lokaatio = requests.get(lokaatiokysely).json()
if len(lokaatio) == 0:
    exit("lokaatiota ei löytnyt")
koordinaatit = (lokaatio[0]["lon"], lokaatio[0]["lat"])
try:
    sääkysely = f"https://api.openweathermap.org/data/2.5/weather?lat={koordinaatit[1]}&lon={koordinaatit[0]}&appid={apikey}&units=metric"
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
sää = requests.get(sääkysely).json()
temperature = sää["main"]["temp"]
säätila = sää["weather"][0]["main"]
print(f"säätila: {säätila}\nlämpötila: {temperature}C")
